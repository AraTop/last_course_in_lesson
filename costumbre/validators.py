from django.core.exceptions import ValidationError


class LimitTime:
    def __init__(self, field_name, max_seconds):
        self.field_name = field_name
        self.max_seconds = max_seconds

    def __call__(self, attrs):
        time_complete = attrs.get(self.field_name)
        time_complete_seconds = time_complete * 60

        if time_complete_seconds > self.max_seconds:
            raise ValidationError(
                f'Поле "{self.field_name}" не может быть больше {self.max_seconds} секунд.'
                    )


class RelatedHabitorReward:
    def __init__(self, related_field, reward_field):
        self.related_field = related_field
        self.reward_field = reward_field

    def __call__(self, data):
        related_value = data.get(self.related_field)
        reward_value = data.get(self.reward_field)

        if related_value and reward_value:
            raise ValidationError(
                f'Можно заполнить только одно из полей: {self.related_field} или {self.reward_field}'
                    )


class Limitdays:
    def __init__(self, field_name, max_days):
        self.field_name = field_name
        self.max_days = max_days

    def __call__(self, data):
        field_name = data.get(self.field_name)
        print(self.max_days)
        if field_name > self.max_days:
            raise ValidationError(
                f'Этот параметр --> {self.field_name}:{field_name} <-- не должен быть больше {self.max_days}'
                    )


class LimitHabits:
    def __init__(self, field_name_1, field_name_2, field_name_3):
        self.field_name_1 = field_name_1
        self.field_name_2 = field_name_2
        self.field_name_3 = field_name_3

    def __call__(self, data):
        field_name_1 = data.get(self.field_name_1)
        field_name_2 = data.get(self.field_name_2)
        field_name_3 = data.get(self.field_name_3)

        if field_name_1 and (field_name_2 or field_name_3):
            raise ValidationError(
                f'Должно быть или:{self.field_name_1}, или это: {self.field_name_2}, {self.field_name_3}'
                    )
