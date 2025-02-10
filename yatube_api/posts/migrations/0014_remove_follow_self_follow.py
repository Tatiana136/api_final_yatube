from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_follow_self_follow'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='self_follow',
        ),
    ]
