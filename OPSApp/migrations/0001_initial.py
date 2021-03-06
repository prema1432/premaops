# Generated by Django 2.2.6 on 2020-05-27 06:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designatation', models.CharField(max_length=100)),
                ('degrees', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='Guideimages/')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designatation', models.CharField(max_length=100)),
                ('degrees', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='Hodimages/')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
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
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=50)),
                ('hallticket', models.BigIntegerField()),
                ('course', models.CharField(choices=[('MCA', 'MCA')], default='MCA', max_length=200)),
                ('semester', models.CharField(choices=[('Third', 'Third'), ('Fourth', 'Fourth'), ('Fifth', 'Fifth'), ('Six', 'Six')], default='Fourth', max_length=200)),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=50)),
                ('DOB', models.DateField(default='1998-01-01')),
                ('phone', models.BigIntegerField()),
                ('technology', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='Stuimages/')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='pupload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptitle', models.CharField(max_length=200)),
                ('pdescription', models.TextField()),
                ('pphoto', models.ImageField(upload_to='Projects/photos/')),
                ('pabstract', models.FileField(upload_to='Project/Abstracts/')),
                ('plive', models.CharField(blank=True, max_length=250)),
                ('pshare', models.CharField(max_length=250)),
                ('photo_1', models.ImageField(blank=True, upload_to='Projects/photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='Projects/photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='Projects/photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='Projects/photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='Projects/photos/%Y/%m/%d/')),
                ('pdate', models.DateTimeField(auto_now_add=True)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guide', to='OPSApp.Guide')),
                ('hod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hod', to='OPSApp.Hod')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pupload', to='OPSApp.Student')),
            ],
        ),
        migrations.AddField(
            model_name='hod',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hod', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='guide',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guide', to=settings.AUTH_USER_MODEL),
        ),
    ]
