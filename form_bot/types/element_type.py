class ElementType:
    NAME = 'name'
    EMAIL = 'email'
    RADIO = 'radio'
    AGE = 'age'
    CHECKBOX = 'checkbox'
    GENDER = 'gender'
    TEXT = 'text'
    SUBMIT = 'submit'

    @staticmethod
    def is_gender(elementType: str):
        return elementType == ElementType.GENDER

    @staticmethod
    def is_name(elementType: str):
        return elementType == ElementType.NAME
    
    @staticmethod
    def is_age(elementType: str):
        return elementType == ElementType.AGE
    
    @staticmethod
    def is_mail(elementType: str):
        return elementType == ElementType.EMAIL

    @staticmethod
    def is_text(elementType: str):
        return elementType in [ElementType.NAME, ElementType.TEXT, ElementType.AGE, ElementType.EMAIL]

    @staticmethod
    def is_submit(elementType: str) -> bool:
        return elementType == ElementType.SUBMIT

    @staticmethod
    def is_radio(elementType: str) -> bool:
        return elementType == ElementType.RADIO

    @staticmethod
    def is_check(elementType: str) -> bool:
        return elementType == ElementType.CHECKBOX

    @staticmethod
    def assert_valid(elementType: str):
        assert elementType in [
            ElementType.NAME,
            ElementType.EMAIL,
            ElementType.RADIO,
            ElementType.AGE,
            ElementType.CHECKBOX,
            ElementType.GENDER,
            ElementType.TEXT,
            ElementType.SUBMIT,
        ]
