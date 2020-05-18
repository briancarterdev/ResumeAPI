# Generated by Django 3.0.6 on 2020-05-19 00:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import education.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('description', models.TextField()),
                ('featured', models.BooleanField()),
                ('name', models.CharField(max_length=100)),
                ('semester', models.IntegerField(choices=[(1, 'Fall'), (2, 'Winter'), (3, 'Spring'), (4, 'Summer')])),
                ('stub', models.CharField(max_length=10, unique=True)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(2015), education.models.max_value_validator_current_year])),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.School')),
            ],
        ),
    ]
