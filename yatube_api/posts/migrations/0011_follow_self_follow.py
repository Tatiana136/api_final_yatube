from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_post_group'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.F('user') != models.F('following'), name='self_follow'),
        ),
    ]
