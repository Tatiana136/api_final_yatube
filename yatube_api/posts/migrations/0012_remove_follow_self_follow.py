from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_follow_self_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='self_follow',
            constraints=['constraints'],
        ),
    ]
