# Generated by Django 3.0.2 on 2020-01-19 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('job', models.IntegerField(
                    choices=[(1, '法师'), (2, '猎人'), (3, '战士'), (4, '萨满祭司'), (5, '德鲁伊'), (6, '牧师'), (7, '潜行者'),
                             (8, '圣骑士'), (9, '术士'), (10, '污手党（猎人、战士、圣骑士）'), (11, '暗金教（法师、牧师、术士）'),
                             (12, '青莲帮（萨满祭司、德鲁伊、潜行者）'), (13, '中立'), (14, '衍生')])),
                ('rarity', models.IntegerField(
                    choices=[(1, '基本（无色）'), (2, '普通（白色）'), (3, '稀有（蓝色)'), (4, '史诗（紫色）'), (5, '传说（橙色）'),
                             (6, '衍生（无色）')])),
                ('effect', models.CharField(max_length=800)),
                ('explanation', models.CharField(max_length=800, null=True)),
                ('attack', models.IntegerField()),
                ('durability', models.IntegerField(default=1)),
                ('pub_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.Version')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Minion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('job', models.IntegerField(
                    choices=[(1, '法师'), (2, '猎人'), (3, '战士'), (4, '萨满祭司'), (5, '德鲁伊'), (6, '牧师'), (7, '潜行者'),
                             (8, '圣骑士'), (9, '术士'), (10, '污手党（猎人、战士、圣骑士）'), (11, '暗金教（法师、牧师、术士）'),
                             (12, '青莲帮（萨满祭司、德鲁伊、潜行者）'), (13, '中立'), (14, '衍生')])),
                ('rarity', models.IntegerField(
                    choices=[(1, '基本（无色）'), (2, '普通（白色）'), (3, '稀有（蓝色)'), (4, '史诗（紫色）'), (5, '传说（橙色）'),
                             (6, '衍生（无色）')])),
                ('effect', models.CharField(max_length=800)),
                ('explanation', models.CharField(max_length=800, null=True)),
                ('attack', models.IntegerField()),
                ('health', models.IntegerField()),
                ('type', models.IntegerField(
                    choices=[(1, '无'), (2, '野兽'), (3, '恶魔'), (4, '元素'), (5, '龙'), (6, '鱼人'), (7, '机械'), (8, '海盗'),
                             (9, '图腾'), (10, '全部')])),
                ('pub_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.Version')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Magic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('job', models.IntegerField(
                    choices=[(1, '法师'), (2, '猎人'), (3, '战士'), (4, '萨满祭司'), (5, '德鲁伊'), (6, '牧师'), (7, '潜行者'),
                             (8, '圣骑士'), (9, '术士'), (10, '污手党（猎人、战士、圣骑士）'), (11, '暗金教（法师、牧师、术士）'),
                             (12, '青莲帮（萨满祭司、德鲁伊、潜行者）'), (13, '中立'), (14, '衍生')])),
                ('rarity', models.IntegerField(
                    choices=[(1, '基本（无色）'), (2, '普通（白色）'), (3, '稀有（蓝色)'), (4, '史诗（紫色）'), (5, '传说（橙色）'),
                             (6, '衍生（无色）')])),
                ('effect', models.CharField(max_length=800)),
                ('explanation', models.CharField(max_length=800, null=True)),
                ('pub_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.Version')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.IntegerField()),
                ('job', models.IntegerField(
                    choices=[(1, '法师'), (2, '猎人'), (3, '战士'), (4, '萨满祭司'), (5, '德鲁伊'), (6, '牧师'), (7, '潜行者'),
                             (8, '圣骑士'), (9, '术士'), (10, '污手党（猎人、战士、圣骑士）'), (11, '暗金教（法师、牧师、术士）'),
                             (12, '青莲帮（萨满祭司、德鲁伊、潜行者）'), (13, '中立'), (14, '衍生')])),
                ('rarity', models.IntegerField(
                    choices=[(1, '基本（无色）'), (2, '普通（白色）'), (3, '稀有（蓝色)'), (4, '史诗（紫色）'), (5, '传说（橙色）'),
                             (6, '衍生（无色）')])),
                ('effect', models.CharField(max_length=800)),
                ('explanation', models.CharField(max_length=800, null=True)),
                ('skill_name', models.CharField(max_length=50)),
                ('skill_cost', models.IntegerField(null=True)),
                ('skill', models.CharField(max_length=400)),
                ('pub_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hs.Version')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
