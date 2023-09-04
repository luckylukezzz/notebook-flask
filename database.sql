CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150) UNIQUE,
    password VARCHAR(150),
    first_name VARCHAR(150)
);

CREATE TABLE Note (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data TEXT,
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES User(id)
);




-- Insert random data into the User table
INSERT INTO User (email, password, first_name)
VALUES
    ('user1@example.com', 'password1', 'John'),
    ('user2@example.com', 'password2', 'Alice'),
    ('user3@example.com', 'password3', 'Bob'),
    ('user4@example.com', 'password4', 'Eve');

-- Insert random data into the Note table
INSERT INTO Note (data, user_id)
VALUES
    ('This is a note from user 1', 1),
    ('A note from user 2', 2),
    ('Note 3 by user 3', 3),
    ('User 4 wrote this note', 4);
