#list
#sequencial 
#indexed
#data mutable
#duplicates allowed
#heterogenous

Data = [11,21,51,101,3.14];
print(type(Data));
print("Original Data",Data);
print("Len of list is ",len(Data));

print("Data from 0th index:",Data[0]);
print("Data from 1st index:",Data[1]);

Data[0] = 12;

print(Data[0]);

Data.append(200);
print(Data);

Data.insert(2,51);
print(Data);

print(Data[-1]);
print(Data[-2]);

print(Data[1:3]);
print(Data[0:4]);
