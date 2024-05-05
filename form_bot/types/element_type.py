class ElementType:
    NAME = 'name'
    RADIO = 'radio'
    CHECKBOX = 'checkbox'
    GENDER = 'gender'
    TEXT = 'text'
    SUBMIT = 'submit'

    @staticmethod
    def is_text(elementType: str):
        return elementType in [ElementType.NAME, ElementType.GENDER, ElementType.TEXT]

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
            ElementType.RADIO,
            ElementType.CHECKBOX,
            ElementType.GENDER,
            ElementType.TEXT,
            ElementType.SUBMIT
        ]
