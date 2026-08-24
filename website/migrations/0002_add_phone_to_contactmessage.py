from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactmessage",
            name="phone",
            field=models.CharField(
                max_length=30,
                blank=True,
                default=""
            ),
            preserve_default=False,
        ),
    ]