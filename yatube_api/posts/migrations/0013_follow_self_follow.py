from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_follow_self_follow'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='follow',
            remove_constraints=True,
        ),
    ]
