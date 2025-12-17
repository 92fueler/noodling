from typing import List
from dataclasses import dataclass 
from datetime import datetime, timedelta

# ============================================
# DATA CLASSES
# ============================================

@dataclass
class Book:
    id: int
    author: str
    name: str
    is_available: bool = True

    def checkout_book(self): 
        if not self.is_available:
            raise ValueError(f"{self.name} is already checked out!")
        self.is_available = False

    def return_book(self):
        self.is_available = True


@dataclass 
class Member:
    id: int 
    name: str


@dataclass
class Loan:
    """Tracks who borrowed what book and when"""
    book: Book
    member: Member
    checkout_date: datetime
    due_date: datetime
    returned: bool = False
    
    @classmethod
    def create(cls, book: Book, member: Member, loan_days: int = 14):
        """Factory method - easier way to create a loan"""
        now = datetime.now()
        return cls(
            book=book,
            member=member,
            checkout_date=now,
            due_date=now + timedelta(days=loan_days),
            returned=False
        )
    
    def is_overdue(self) -> bool:
        """Check if the loan is past its due date"""
        return not self.returned and datetime.now() > self.due_date
    
    def return_book(self):
        """Process the return"""
        self.returned = True
        self.book.return_book()
    
    def days_until_due(self) -> int:
        """How many days until due (negative if overdue)"""
        if self.returned:
            return 0
        delta = self.due_date - datetime.now()
        return delta.days


# ============================================
# BEHAVIOR CLASS
# ============================================

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.loans: List[Loan] = []  # ← Track all loans!

        # Add some test books
        for idx in range(3):
            self.books.append(
                Book(id=idx, author=f"Author{idx}", name=f"Book{idx}")
            )
        
        # Add some test members
        for idx in range(10, 12):
            self.members.append(Member(id=idx, name=f"Member{idx}"))

    def register_member(self, member: Member):
        """Add a new member"""
        self.members.append(member)
        print(f"✅ Registered: {member.name}")
        
    def add_book(self, book: Book):
        """Add a new book"""
        self.books.append(book)
        print(f"✅ Added book: {book.name}")
    
    def checkout_book(self, member: Member, book: Book) -> Loan:
        """Let a member borrow a book"""
        # Validate book is in library
        if book not in self.books:
            raise ValueError("Book not in this library")
        
        # Validate member is registered
        if member not in self.members:
            raise ValueError("Member not registered")
        
        # Try to checkout (this validates availability)
        book.checkout_book()
        
        # Create the loan
        loan = Loan.create(book, member)
        self.loans.append(loan)
        
        print(f"📚 {member.name} checked out '{book.name}'")
        print(f"   Due date: {loan.due_date.strftime('%Y-%m-%d')}")
        
        return loan
    
    def return_book(self, loan: Loan):
        """Process a book return"""
        loan.return_book()
        
        print(f"📖 {loan.member.name} returned '{loan.book.name}'")
        
        if loan.is_overdue():
            print(f"   ⚠️  Book was overdue!")
        else:
            print(f"   ✅ Returned on time")
    
    def list_available_books(self):
        """Show all books currently available"""
        print("\n📚 Available Books:")
        available = [book for book in self.books if book.is_available]
        
        if not available:
            print("   (none)")
        else:
            for book in available:
                print(f"   - {book.name} by {book.author}")
    
    def list_active_loans(self):
        """Show all currently checked out books"""
        print("\n📋 Active Loans:")
        active = [loan for loan in self.loans if not loan.returned]
        
        if not active:
            print("   (none)")
        else:
            for loan in active:
                status = "⚠️ OVERDUE" if loan.is_overdue() else f"Due in {loan.days_until_due()} days"
                print(f"   - {loan.book.name} → {loan.member.name} ({status})")
    
    def get_member_loans(self, member: Member) -> List[Loan]:
        """Get all loans for a specific member"""
        return [loan for loan in self.loans if loan.member == member]
    
    def get_overdue_loans(self) -> List[Loan]:
        """Get all overdue loans"""
        return [loan for loan in self.loans if loan.is_overdue()]


# ============================================
# DEMO
# ============================================

def main():
    print("="*60)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*60)
    
    # Create library
    library = Library()
    
    # Add a custom book
    custom_book = Book(id=99, author="George Orwell", name="1984")
    library.add_book(custom_book)
    
    # Add a custom member
    alice = Member(id=1, name="Alice")
    library.register_member(alice)
    
    print("\n" + "="*60)
    
    # Show available books
    library.list_available_books()
    
    print("\n" + "="*60)
    
    # Alice borrows a book
    loan1 = library.checkout_book(library.members[0], library.books[0])
    
    # Member10 borrows another book
    loan2 = library.checkout_book(library.members[1], custom_book)
    
    print("\n" + "="*60)
    
    # Show current status
    library.list_available_books()
    library.list_active_loans()
    
    print("\n" + "="*60)
    
    # Alice returns her book
    library.return_book(loan1)
    
    print("\n" + "="*60)
    
    # Show final status
    library.list_available_books()
    library.list_active_loans()
    
    print("\n" + "="*60)
    
    # Check Alice's loan history
    print(f"\n📜 {alice.name}'s Loan History:")
    alice_loans = library.get_member_loans(alice)
    for loan in alice_loans:
        status = "Returned" if loan.returned else "Active"
        print(f"   - {loan.book.name} ({status})")


if __name__ == "__main__":
    main()
    