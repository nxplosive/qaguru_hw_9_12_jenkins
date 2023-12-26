import dataclasses


@dataclasses.dataclass
class User:
    firstName: str
    lastName: str
    userEmail: str
    userGender: str
    userPhoneNumber: str
    month: str
    year: str
    day: str
    userSubject: str
    userHobby: str
    userPicture: str
    userCurrentAddress: str
    userState: str
    userCity: str


guest = User(
    firstName='Nikita',
    lastName='Safonov',
    userEmail='nicksaff@gmail.com',
    userGender='Male',
    userPhoneNumber='9151232211',
    month='December',
    year='1990',
    day='15',
    userSubject='English',
    userHobby='Sports',
    userPicture='avatar.jpg',
    userCurrentAddress='Zombie Land',
    userState='NCR',
    userCity='Noida',
)
