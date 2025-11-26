# 🏥 Hospital Management System (Tkinter & MySQL)

This project is a simple **Hospital Management System** developed using **Python's Tkinter** for the graphical user interface and **MySQL** for data persistence. It allows users to input, view, generate prescriptions, update, and delete patient and medication records.

---
## 🖼️ Architectural Flowchart

This diagram illustrates the data and control flow between the **Client Tier (Python/Tkinter)** and the **Data Tier (MySQL)** when a user performs a typical CRUD operation (Create, Read, Update, Delete).

### Data Flow Diagram (Mermaid Syntax)

To view this diagram, you may need a Markdown viewer that supports the [Mermaid extension](https://mermaid.js.org/).

```mermaid

graph TD
    subgraph Client Tier (Python Application)
        A[User Interaction: Button Click (e.g., Prescription Data)]
        B{Hospital Class Methods}
        C[Gather Data from Tkinter Variables]
        D[mysql.connector: Execute SQL Query]
    end

    subgraph Interface
        E[MySQL Connector API] --> F[Connection Object]
    end

    subgraph Data Tier (MySQL Server)
        G[hospital_data Database]
        H[Data Table (Storage)]
        I[Result Set / Status (Success/Error)]
    end

    A --> B
    B --> C
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H{CRUD Operation: INSERT, UPDATE, SELECT}
    H --> I
    I --> D
    D --> B
    B --> J[Update UI: Show success/error message & Refresh Table]

    style A fill:#D0E7FF,stroke:#333
    style J fill:#D0E7FF,stroke:#333
    style B fill:#FFE0B2,stroke:#333
    style C fill:#FFFDE7,stroke:#333
    style D fill:#FFE0B2,stroke:#333
    style E fill:#B2EBF2,stroke:#333
    style F fill:#B2EBF2,stroke:#333
    style G fill:#E0F7FA,stroke:#333
    style H fill:#E0F7FA,stroke:#333
    style I fill:#E0F7FA,stroke:#333
```
