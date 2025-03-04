# Generated by Django 4.2.19 on 2025-03-04 22:01

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('fitness_goal', models.CharField(choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('endurance', 'Endurance'), ('general_fitness', 'General Fitness')], default='general_fitness', max_length=100)),
                ('workout_location', models.CharField(choices=[('home', 'Home'), ('gym', 'Gym')], default='gym', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('goal', models.CharField(choices=[('strength', 'Strength'), ('cardio', 'Cardio'), ('hypertrophy', 'Hypertrophy'), ('fat_loss', 'Fat Loss')], max_length=100)),
                ('duration', models.IntegerField(default=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_plans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('day_of_week', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10)),
                ('workout_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workout_sessions', to='core.workoutplan')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_location', models.CharField(choices=[('gym', 'Gym'), ('home', 'Home')], max_length=10)),
                ('available_equipment', models.JSONField(default=list)),
                ('fitness_goal', models.CharField(choices=[('weight_loss', 'Weight Loss'), ('muscle_gain', 'Muscle Gain'), ('endurance', 'Endurance'), ('general_fitness', 'General Fitness')], max_length=50)),
                ('experience_level', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], max_length=20)),
                ('days_per_week', models.IntegerField(default=3)),
                ('health_conditions', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='preferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NutritionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_calories', models.IntegerField()),
                ('protein_g', models.FloatField()),
                ('carbs_g', models.FloatField()),
                ('fats_g', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrition_plans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('calories', models.IntegerField()),
                ('protein_g', models.FloatField()),
                ('carbs_g', models.FloatField()),
                ('fats_g', models.FloatField()),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=50)),
                ('nutrition_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='core.nutritionplan')),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sets', models.PositiveIntegerField(default=2)),
                ('reps', models.PositiveIntegerField(default=10)),
                ('rest_time', models.PositiveIntegerField(default=60)),
                ('equipment_needed', models.CharField(blank=True, max_length=255, null=True)),
                ('muscle_group', models.CharField(choices=[('chest', 'Chest'), ('back', 'Back'), ('legs', 'Legs'), ('arms', 'Arms'), ('shoulders', 'Shoulders'), ('abs', 'Abs'), ('core', 'Core'), ('other', 'Other'), ('none', 'None'), ('full_body', 'Full Body')], default='none', max_length=100)),
                ('workout_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='core.workoutsession')),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('workout_completed', models.BooleanField(default=False)),
                ('meals_followed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
