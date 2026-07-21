## 1. Use cases

1. A student can search the book by title and author 
2. librarian can issue the book to the student 
6. when new book is avaliable then librarian will add this book show it availble to all students 
7. When the student time is over than he return back and librarian close this opening and book is avaliable for another students
8. Student can enter into the system by Regiter on the portal
9. A student can view there due date of the book 
10. Student pay the fine to department by hand than librarian marked as received and the system update.

## 2. Business Rules
4. if student  borrow a book and not retun within 14 days than we will fine it for 2% everyday on the MRP 
5. Maximum book for student is 3 more than books are not allowed
10. If the book is damage than 100 RS fine 


## 3.Edge Case
3. Another student also search the same book but the book is already taken by another student so there is Unavailable of the book

## 4. Entities

### Book (catalog info — one per title)
Attributes:
- id
- title
- author
- mrp            → needed by Business Rule 1 (fine = 2% of MRP)

### BookCopy (one physical copy on the shelf)
Attributes:
- id
- book_id        → which Book this copy belongs to
- status         → AVAILABLE / ISSUED / DAMAGED / REMOVED

### Student
Attributes:
- id
- name
- email
- registered_on
Behaviors:
- can_borrow_more()   → false if already has 3 active loans (Business Rule 2)
- has_unpaid_fine()   → true if any fine is PENDING

### Librarian
Attributes:
- id
- name
- email

### Loan (my "opening" — connects Student and BookCopy)
Attributes:
- id
- student_id
- copy_id        → NOTE: copy, not book!
- issue_date
- due_date       → issue_date + 14 days (Business Rule 1)
- return_date    → empty until the student returns it
Behaviors:
- is_overdue()   → today > due_date and not yet returned

### Fine
Attributes:
- id
- loan_id        → which loan caused this fine
- amount
- reason         → LATE / DAMAGE
- status         → PENDING / PAID


