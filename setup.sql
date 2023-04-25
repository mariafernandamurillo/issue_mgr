CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash something",
    "Do something"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash something 2",
    "Do something 2"
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash something 3",
    "Do something 3"
);

