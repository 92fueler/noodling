# Library Management System - Design

## 1. What We're Building
A library system where:
- Books can be borrowed and returned by members
- System tracks checkout status and due dates
- System can search for books and members
- System identifies overdue books

---

## 2. Core Entities

### Book (Dataclass - Data)
**What**: Physical book in the library
**Attributes**:
- id: int
- title: str
- author: str
- is_available: bool = True

**Methods**:
- checkout() - mark unavailable
- return_book() - mark available

---

### Member (Dataclass - Data)
**What**: Library member who can borrow books
**Attributes**:
- id: int
- name: str
- email: str

**Methods**: (none - just data)

---

### Loan (Dataclass - Data with helpers)
**What**: Record of a book borrowing transaction
**Attributes**:
- book: Book
- member: Member
- checkout_date: datetime
- due_date: datetime
- returned: bool = False

**Methods**:
- @classmethod create(book, member, days=14) - factory
- is_overdue() -> bool
- return_book() - mark returned and update book

---

### Library (Regular Class - Behavior)
**What**: Orchestrator managing books, members, and loans
**Attributes**:
- books: List[Book]
- members: List[Member]
- loans: List[Loan]

**Methods**:

*Adding entities:*
- add_book(book: Book)
- register_member(member: Member)

*Core operations:*
- checkout_book(member: Member, book: Book) -> Loan
- return_book(loan: Loan)

*Search operations:*
- find_book_by_id(id: int) -> Book | None
- find_book_by_title(title: str) -> List[Book]
- find_book_by_author(author: str) -> List[Book]
- find_member_by_id(id: int) -> Member | None
- find_member_by_name(name: str) -> List[Member]

*Listing operations:*
- list_available_books() -> List[Book]
- list_active_loans() -> List[Loan]
- list_overdue_loans() -> List[Loan]
- get_member_loans(member: Member) -> List[Loan]

---

## 3. Relationships (How they connect)
```
Library HAS-MANY Books
Library HAS-MANY Members
Library HAS-MANY Loans

Loan HAS-A Book (reference)
Loan HAS-A Member (reference)

Book USES-BY Loan (indirectly)
Member BORROWS-THROUGH Loan
```

---

## 4. Data Flow

### Checkout Flow:
1. User calls: `library.checkout_book(member, book)`
2. Library validates: book available? member registered?
3. Book marks itself unavailable: `book.checkout()`
4. Loan created: `Loan.create(book, member)`
5. Library stores loan: `loans.append(loan)`

### Return Flow:
1. User calls: `library.return_book(loan)`
2. Loan marks itself returned: `loan.return_book()`
3. Book marks itself available: `book.return_book()`
4. Loan stays in history (for tracking)

---

## 5. Key Design Decisions

**Why Dataclass for Book/Member/Loan?**
- Primarily store data
- Need `__eq__` and `__repr__` (dataclass provides free)
- Few methods (mostly getters/simple logic)

**Why Regular Class for Library?**
- Primarily behavior/coordination
- Many methods
- Manages relationships between entities

**Why separate Loan class?**
- Represents relationship between Book and Member
- Tracks temporal data (dates)
- Enables loan history tracking
```

---

## 📊 Visual Summary
```
┌─────────────────────────────────────────┐
│           LIBRARY (Manager)             │
│  Responsibilities:                      │
│  - Add books/members                    │
│  - Checkout/return                      │
│  - Search                               │
│  - Generate reports                     │
└──────┬──────────────┬───────────────┬───┘
       │              │               │
       ▼              ▼               ▼
   ┌───────┐     ┌─────────┐    ┌────────┐
   │ BOOK  │     │ MEMBER  │    │  LOAN  │
   │ Data  │     │  Data   │    │  Data  │
   └───────┘     └─────────┘    └────────┘
       ▲              ▲               │
       │              │               │
       └──────────────┴───────────────┘
              Referenced by Loan
