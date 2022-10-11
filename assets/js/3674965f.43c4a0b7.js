"use strict";(self.webpackChunkmy_website=self.webpackChunkmy_website||[]).push([[9993],{4846:(e,a,n)=>{n.r(a),n.d(a,{contentTitle:()=>c,default:()=>d,frontMatter:()=>r,metadata:()=>h,toc:()=>m});var t=n(7462),s=n(7294),l=n(3905),i=n(7273);i.Z.initialize({startOnLoad:!0});const o=e=>{let{chart:a}=e;return(0,s.useEffect)((()=>{i.Z.contentLoaded()}),[]),s.createElement("div",{className:"mermaid"},a)},r={},c=void 0,h={type:"mdx",permalink:"/Python/doc1",source:"@site/src/pages/doc1.md",frontMatter:{}},m=[{value:"Sequence Graph",id:"sequence-graph",level:2},{value:"Class Diagram",id:"class-diagram",level:2},{value:"Entity Relationship Diagram",id:"entity-relationship-diagram",level:2}],p={toc:m};function d(e){let{components:a,...n}=e;return(0,l.kt)("wrapper",(0,t.Z)({},p,n,{components:a,mdxType:"MDXLayout"}),(0,l.kt)(o,{chart:"\n\tgraph LR;\n\t\tA--\x3eB;\n\t\tB--\x3eC;\n\t\tB--\x3eD[plop lanflz eknlzeknfz];\n",mdxType:"Mermaid"}),(0,l.kt)("h2",{id:"sequence-graph"},"Sequence Graph"),(0,l.kt)(o,{chart:"\nsequenceDiagram;\n    participant Alice\n    participant Bob\n    Alice->>John: Hello John, how are you?\n    loop Healthcheck\n        John->>John: Fight against hypochondria\n    end\n    Note right of John: Rational thoughts <br/>prevail!\n    John--\x3e>Alice: Great!\n    John->>Bob: How about you?\n    Bob--\x3e>John: Jolly good!\n",mdxType:"Mermaid"}),(0,l.kt)("h2",{id:"class-diagram"},"Class Diagram"),(0,l.kt)(o,{chart:"\nclassDiagram\nClass01 <|-- AveryLongClass : Cool\nClass03 *-- Class04\nClass05 o-- Class06\nClass07 .. Class08\nClass09 --\x3e C2 : Where am i?\nClass09 --* C3\nClass09 --|> Class07\nClass07 : equals()\nClass07 : Object[] elementData\nClass01 : size()\nClass01 : int chimp\nClass01 : int gorilla\nClass08 <--\x3e C2: Cool label\n",mdxType:"Mermaid"}),(0,l.kt)("h2",{id:"entity-relationship-diagram"},"Entity Relationship Diagram"),(0,l.kt)(o,{chart:"\nerDiagram\n    CUSTOMER ||--o{ ORDER : places\n    ORDER ||--|{ LINE-ITEM : contains\n    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses\n",mdxType:"Mermaid"}))}d.isMDXComponent=!0}}]);