# Kafka vs RabbitMQ Workflow Comparison

Visual workflow comparison using Mermaid diagrams.

## Kafka Architecture

```mermaid
%% Kafka Workflow
graph TD
    subgraph Kafka_Cluster
        B[("Broker (Node 1)")]
        B2[("Broker (Node 2)")]
        B3[("Broker (Node 3)")]
    end
    
    P1[Producer] -->|Publish to| T1[Topic A]
    P2[Producer] -->|Publish to| T2[Topic B]
    
    subgraph Topics
        T1 --> P0[Partition 0]
        T1 --> P1[Partition 1]
        T2 --> P2[Partition 0]
    end
    
    P0 --> CG1[Consumer Group 1]
    P1 --> CG2[Consumer Group 2]
    P2 --> CG1
```

**Key Components:**
- Producers publish to partitioned topics
- Brokers store messages in partitions
- Consumer groups subscribe to partitions
- Messages persist based on retention policy

## RabbitMQ Architecture

```mermaid
%% RabbitMQ Workflow
graph TD
    P[Producer] --> Ex[Exchange]
    
    subgraph Exchange_Types
        Ex --> D[Direct]
        Ex --> T[Topic]
        Ex --> F[Fanout]
        Ex --> H[Headers]
    end
    
    D --> Q1[Queue 1]
    T --> Q2[Queue 2]
    F --> Q3[Queue 3]
    H --> Q4[Queue 4]
    
    Q1 --> C1[Consumer]
    Q2 --> C2[Consumer]
    Q3 --> C3[Consumer]
    Q4 --> C4[Consumer]
```

**Key Components:**
- Producers send to exchanges
- Exchanges route to queues based on type/bindings
- Consumers subscribe to queues
- Messages deleted after acknowledgment

## Side-by-Side Comparison

```mermaid
%% Comparison Diagram
graph LR
    subgraph Kafka
        KP[Producer] --> KT[Topic]
        KT --> KP1[Partition 1]
        KT --> KP2[Partition 2]
        KP1 --> KCG[Consumer Group]
        KP2 --> KCG
    end
    
    subgraph RabbitMQ
        RP[Producer] --> RX[Exchange]
        RX --> RQ1[Queue 1]
        RX --> RQ2[Queue 2]
        RQ1 --> RC[Consumer]
        RQ2 --> RC
    end
```

| Feature          | Kafka                          | RabbitMQ                     |
|------------------|--------------------------------|------------------------------|
| **Message Model**| Persistent log                 | Temporary queues             |
| **Delivery**     | Pull-based                     | Push-based (default)         |
| **Ordering**     | Per-partition guarantee        | Per-queue FIFO               |
| **Routing**      | Simple (topic/partition)       | Complex (exchange types)     |
| **Scale**        | Horizontal partitioning        | Vertical scaling (sharding)  |

## Message Flow Sequence

### Kafka Sequence

```mermaid
sequenceDiagram
    participant Producer
    participant Broker
    participant Consumer
    
    Producer->>Broker: Produce (key, value)
    Broker->>Broker: Write to partition log
    Consumer->>Broker: Poll request
    Broker->>Consumer: Return message batch
    Consumer->>Broker: Commit offset
```

### RabbitMQ Sequence

```mermaid
sequenceDiagram
    participant Producer
    participant Exchange
    participant Queue
    participant Consumer
    
    Producer->>Exchange: Publish (routing key)
    Exchange->>Queue: Route via bindings
    Queue->>Consumer: Deliver message (push)
    Consumer->>Queue: Send ACK/NACK
    alt ACK
        Queue->>Queue: Delete message
    else NACK
        Queue->>Queue: Requeue message
    end
```

## Failure Handling Comparison

```mermaid
flowchart TB
    subgraph Kafka_Failure
        KF[Consumer Fails] --> KR[Next poll continues from last offset]
        KR --> KA[No message loss]
    end
    
    subgraph RabbitMQ_Failure
        RF[Consumer Fails] --> RR[Unacked message returned to queue]
        RR --> RA[Message redelivered]
    end
```

**Installation Note:**  
GitHub natively supports Mermaid diagrams. For local viewing:
1. VS Code: Install "Mermaid Preview" extension
2. Online: Use [Mermaid Live Editor](https://mermaid.live)

