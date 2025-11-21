graph TD
    %% --- STYLES ---
    classDef core fill:#2d3436,stroke:#00b894,stroke-width:2px,color:white;
    classDef switch fill:#0984e3,stroke:none,color:white;
    classDef device fill:#dfe6e9,stroke:#2d3436,color:black;
    classDef fiber stroke:#d63031,stroke-width:3px;

    %% --- NODES ---
    ISP[ISP Fiber]:::core
    UDM[UDM-Pro Gateway]:::core
    AGG[USW-Aggregation]:::core
    
    subgraph "Office Rack (Ecoflow Power)"
        UDM
        AGG
        ENT[USW-Enterprise-24-PoE]:::switch
        SERVER[i9 Server Node 1]:::device
        NUC[NUC 10 Node 2]:::device
        PI[Pi 5 Witness]:::device
        UNVR[UniFi UNVR]:::device
    end

    subgraph "Staircase Distribution"
        FLEX25[Flex 2.5G Switch]:::switch
        U7[U7 Pro AP]:::device
    end

    subgraph "Rooms & Outdoor"
        FLEXMINI[Flex Mini]:::switch
        LITE8[Lite 8 PoE]:::switch
        FLEXOUT[Flex Outdoor]:::switch
        CAMS[Cameras]:::device
    end

    %% --- CONNECTIONS ---
    ISP --> UDM
    UDM -->|10G DAC| AGG
    AGG -->|10G DAC| ENT
    AGG -->|10G DAC| UNVR
    AGG -->|10G RJ45| SERVER
    
    %% The Critical 10G Uplink
    AGG ===|10G Fiber/RJ45 + PoE Injector| FLEX25
    linkStyle 5 class fiber

    %% Downlinks
    ENT -->|2.5GbE| NUC
    ENT -->|1GbE PoE| PI
    
    %% Staircase Distribution
    FLEX25 -->|2.5GbE PoE| U7
    FLEX25 -->|1GbE PoE| FLEXMINI
    FLEX25 -->|1GbE Data| LITE8
    
    %% Outdoor
    ENT -->|PoE++| FLEXOUT
    FLEXOUT --> CAMS
