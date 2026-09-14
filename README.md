# README

## Diagram

+-------------------------------------------------------------------------+
|                             BankingDocument                             |
+--------------------------+-------------------+--------------------------+
| PK                       | id                | BigAutoField             |
|                          | title             | CharField(255)           |
|                          | content           | TextField                |
|                          | document_type     | CharField(50)            |
|                          | status            | CharField(20)            |
|                          | customer_name     | CharField(255)           |
|                          | customer_id       | CharField(100)           |
|                          | embedding         | JSONField (NULL)         |
|                          | metadata          | JSONField                |
|                          | created_at        | DateTimeField            |
|                          | updated_at        | DateTimeField            |
+--------------------------+-------------------+--------------------------+
                                    |
                                    | 1
                                    |
                                    |
                                   / \  (One-to-Many)
                                  /   \
                                 /  M  \
+-------------------------------+-------+---------------------------------+
|                              WorkflowTask                               |
+--------------------------+-------------------+--------------------------+
| PK                       | id                | BigAutoField             |
| FK                       | document_id       | ForeignKey -> BankingDoc |
|                          | task_type         | CharField(50)            |
|                          | description       | TextField                |
|                          | assigned_to       | CharField(255)           |
|                          | is_completed      | BooleanField             |
|                          | created_at        | DateTimeField            |
|                          | completed_at      | DateTimeField (NULL)     |
+--------------------------+-------------------+--------------------------+