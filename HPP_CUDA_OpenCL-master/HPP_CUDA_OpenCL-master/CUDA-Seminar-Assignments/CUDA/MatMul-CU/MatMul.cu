#include <stdio.h>

//cuda headers
#include <cuda.h>
#include "helper_timer.h"

//macros
#define BLOCK_WIDTH 1032

//global variables
int *hostA = NULL;
int *hostB = NULL;
int *hostC = NULL;
int *gold = NULL;

int *deviceA = NULL;
int *deviceB = NULL;
int *deviceC = NULL;

float timeOnCPU = 0.0f;
float timeOnGPU = 0.0f;

// cuda kernel function
__global__ void matMulGPU(int *A, int *B, int *C, int numARows, int numAColumns, int numBColumns, int numCColumns)
{
    //variable declarations
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int column = blockIdx.x * blockDim.x + threadIdx.x;

    // code
    if((row < numARows) && (column < numBColumns))
    {
        int value = 0.0;
        
        for(int k = 0; k < numAColumns; k++)
        {
            int a = A[row * numAColumns + k];
            int b = B[k * numBColumns + column];
            value += a * b;
        }

        C[row * numCColumns + column] = value;
    }

}

int main()
{
    // function declarations
    void InitA(int *data,int,int);
    void InitB(int *data,int,int);
    void matMulCPU(int *, int *, int *, int, int, int, int);
    void cleanup(void);

    // variable declaration
    int numARows = BLOCK_WIDTH;
    int numAColumns = BLOCK_WIDTH;
    int numBRows = BLOCK_WIDTH;
    int numBColumns = BLOCK_WIDTH;
    int numCRows = numARows;
    int numCColumns = numBColumns;

    int numGoldRows = numARows;
    int numGodlColumns = numBColumns;

    int sizeA = numARows * numAColumns * sizeof(int);
    int sizeB = numBRows * numBColumns * sizeof(int);
    int sizeC = numCRows * numBColumns * sizeof(int);
    int sizeGold = numGoldRows * numGodlColumns * sizeof(int);

    cudaError_t result = cudaSuccess;

    //code
    //host memory allocation
    hostA = (int*)malloc(sizeA);
    if (hostA == NULL)
    {
        printf("Host Memory allocation is failed for hostA matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    hostB = (int*)malloc(sizeB);
    if (hostB == NULL)
    {
        printf("Host Memory allocation is failed for hostB matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    hostC = (int*)malloc(sizeC);
    if (hostC == NULL)
    {
        printf("Host Memory allocation is failed for hostC matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    gold = (int*)malloc(sizeGold);
    if (gold == NULL)
    {
        printf("Host Memory allocation is failed for gold matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    // printing matrix dimensions and sizes
    printf("The Dimensions of Matrix 'hostA' are : %d x %d\n",numARows,numAColumns);
    printf("The Dimensions of Matrix 'hostB' are : %d x %d\n",numBRows,numBColumns);
    printf("The Dimensions of Matrix 'hostC' are : %d x %d\n",numCRows,numCColumns);
    printf("The Dimensions of Matrix 'gold' are : %d x %d\n",numGoldRows,numGodlColumns);

    printf("Size of Matrix hostA = %d\n",sizeA);
    printf("Size of Matrix hostB = %d\n",sizeB);
    printf("Size of Matrix hostC = %d\n",sizeC);
    printf("Size of Matrix gold = %d\n",sizeGold);

    // fill source matrices
    InitA(hostA,numARows,numAColumns);
    InitB(hostB,numBRows,numBColumns);

    // device memory allocation
    result = cudaMalloc((void**)&deviceA,sizeA);
    if (result != cudaSuccess)
    {
        printf("Device Memory allocation is failed for deviceA matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    result = cudaMalloc((void**)&deviceB,sizeB);
    if (result != cudaSuccess)
    {
        printf("Device Memory allocation is failed for deviceB array.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    result = cudaMalloc((void**)&deviceC,sizeC);
    if (result != cudaSuccess)
    {
        printf("Device Memory allocation is failed for deviceC array.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    //copy data from host matrices into device matrices
    result = cudaMemcpy(deviceA, hostA, sizeA, cudaMemcpyHostToDevice);
    if (result != cudaSuccess)
    {
        printf("Host to Device Data Copy is failed for deviceA matrix.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    result = cudaMemcpy(deviceB, hostB, sizeB, cudaMemcpyHostToDevice);
    if (result != cudaSuccess)
    {
        printf("Host to Device Data Copy is failed for deviceB array.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }

    // CUDA Kernel configuration
    dim3 dimGrid = dim3(ceil((int)numBColumns / (int)BLOCK_WIDTH), ceil((int)numARows / (int)BLOCK_WIDTH), 1);
    dim3 dimBlock = dim3(BLOCK_WIDTH, BLOCK_WIDTH, 1);

    // cuda kernel for Matrix Multiplication
    StopWatchInterface* timer = NULL;
    sdkCreateTimer(&timer);
    sdkStartTimer(&timer);

    matMulGPU <<<dimGrid, dimBlock >>>(deviceA,deviceB,deviceC,numARows,numAColumns,numBColumns,numCColumns);

    sdkStopTimer(&timer);
    timeOnGPU = sdkGetTimerValue(&timer);
    timer = NULL;

    // copy data from Device to Host
    result = cudaMemcpy(hostC, deviceC, sizeC, cudaMemcpyDeviceToHost);
    if (result != cudaSuccess)
    {
        printf("Device to Host Data copy is failed for deviceC array.\n");
        cleanup();
        exit(EXIT_FAILURE);
    }
    
    // matrix multiplication on host
    matMulCPU(hostA, hostB, gold, numARows, numAColumns, numBColumns, numCColumns);

    // comparison
    int breakValue = -1;
    bool bAccuracy = true;
    for (int i = 0; i < numCRows * numCColumns; i++)
    {
        int val1 = gold[i];
        int val2 = hostC[i];
        if (val1 != val2)
        {
            breakValue = i;
            bAccuracy = false;
            break;
        }
    }

    char str[128];
    if(bAccuracy != true)
    {
        sprintf(str,"Comparison of CPU and GPU Matrix Multiplication is not accurate at array index %d",breakValue);
    }
    else
    {
        sprintf(str,"Comparison of CPU and GPU Matrix Multiplication is accurate");
    }

    printf("Time taken for Matrix Multiplication on CPU = %.6f\n",timeOnCPU);
    printf("Time taken for Matrix Multiplication on GPU = %.6f\n",timeOnGPU);
    printf("%s\n",str);

    // cleanup
    cleanup();

    return (0);
}

void InitA(int *data,int row,int col)
{
    int num = 1;

    //code
    for(int i = 0;i < row; i++)
    {
        for(int j = 0; j < col; j++)
        {
            *(data + i * row + j) = num;
            num++;
        }
    }
}

void InitB(int *data,int row,int col)
{
    int num = BLOCK_WIDTH;
    
    // code
    for (int i = 0; i < row; i++)
    {
        for(int j = 0; j < col; j++)
        {
            *(data + i * row + j) = num;
            num++;
        }
    }
}

void matMulCPU(int* A, int* B, int* C, int numARows, int numAColumns, int numBColumns, int numCColums)
{
    // code
    StopWatchInterface* timer = NULL;
    sdkCreateTimer(&timer);
    sdkStartTimer(&timer);
        
    for (int i = 0; i < numARows; i++)
    {
        for (int j = 0; j < numBColumns; j++)
        {   
            int val = 0;
            for(int k = 0; k < numAColumns; k++)
            {
                int a = A[i * numAColumns + k];
                int b = B[k * numBColumns + j];
                val += a*b;
            }
            C[i* numCColums + j] = val;
        }
    }

    sdkStopTimer(&timer);
    timeOnCPU = sdkGetTimerValue(&timer);
    timer = NULL;
}

void cleanup(void)
{
    // code
    if(deviceC)
    {
        cudaFree(deviceC);
        deviceC = NULL;
    }

    if(deviceB)
    {
        cudaFree(deviceB);
        deviceB = NULL;
    }

    if(deviceA)
    {
        cudaFree(deviceA);
        deviceA = NULL;
    }

    if(gold)
    {
        cudaFree(gold);
        gold = NULL;
    }

    if(hostC)
    {
        cudaFree(hostC);
        hostC = NULL;
    }

    if(hostB)
    {
        cudaFree(hostB);
        hostB = NULL;
    }

    if(hostA)
    {
        cudaFree(hostA);
        hostA = NULL;
    }

}
