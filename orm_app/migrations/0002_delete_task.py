
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Task',
        ),
    ]