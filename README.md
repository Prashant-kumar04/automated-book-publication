📝 Sequence of Steps
sequenceDiagram
    participant U as User
    participant P as Playwright
    participant W as AI Writer
    participant R as AI Reviewer
    participant H as Human Editor
    participant DB as ChromaDB

    U->>P: Provide book URL
    P->>P: Scrape and capture screenshot
    P->>W: Send original text
    W->>R: Submit rewritten draft
    R->>H: Reviewed content
    H->>DB: Save final version with feedback
