# Generated by Django 3.0.2 on 2020-01-25 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allocatedeicdetail',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('mrid', models.CharField(blank=True, db_column='MRID', max_length=250, null=True)),
                ('docstatusvalue', models.CharField(blank=True, db_column='DocStatusValue', max_length=250, null=True)),
                ('attributeinstancecomponent', models.CharField(blank=True, db_column='AttributeInstanceComponent', max_length=250, null=True)),
                ('longnames', models.CharField(blank=True, db_column='LongNames', max_length=250, null=True)),
                ('displaynames', models.CharField(blank=True, db_column='DisplayNames', max_length=250, null=True)),
                ('lastrequestdateandortime', models.DateTimeField(blank=True, db_column='LastRequestDateAndOrTime', null=True)),
                ('deactivaterequestdateandortime', models.DateTimeField(blank=True, db_column='DeactivateRequestDateAndOrTime', null=True)),
                ('marketparticipantstreetaddresscountry', models.CharField(blank=True, db_column='MarketParticipantStreetAddressCountry', max_length=250, null=True)),
                ('marketparticipantacercode', models.CharField(blank=True, db_column='MarketParticipantACERCode', max_length=250, null=True)),
                ('marketparticipantvatcode', models.CharField(blank=True, db_column='MarketParticipantVATcode', max_length=250, null=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=255, null=True)),
                ('eicparentmarketdocumentmrid', models.CharField(blank=True, db_column='EICParentMarketDocumentMRID', max_length=250, null=True)),
                ('elcresponsiblemarketparticipantmrid', models.CharField(blank=True, db_column='ELCResponsibleMarketParticipantMRID', max_length=250, null=True)),
                ('isdeleted', models.TextField(db_column='IsDeleted')),
            ],
            options={
                'db_table': 'allocatedeicdetail',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Areatypecode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('areatypecodetext', models.CharField(blank=True, db_column='AreaTypeCodeText', max_length=255, null=True, unique=True)),
                ('areatypecodenote', models.CharField(blank=True, db_column='AreaTypeCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'areatypecode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mapcode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('mapcodetext', models.CharField(blank=True, db_column='MapCodeText', max_length=255, null=True, unique=True)),
                ('mapcodenote', models.CharField(blank=True, db_column='MapCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'mapcode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Productiontype',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('productiontypetext', models.CharField(blank=True, db_column='ProductionTypeText', max_length=255, null=True, unique=True)),
                ('productiontypenote', models.CharField(blank=True, db_column='ProductionTypeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'productiontype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Resolutioncode',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('resolutioncodetext', models.CharField(blank=True, db_column='ResolutionCodeText', max_length=255, null=True, unique=True)),
                ('resolutioncodenote', models.CharField(blank=True, db_column='ResolutionCodeNote', max_length=255, null=True)),
            ],
            options={
                'db_table': 'resolutioncode',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='UserId', primary_key=True, serialize=False)),
                ('loginname', models.CharField(db_column='LoginName', max_length=40)),
                ('password', models.CharField(db_column='Password', max_length=50)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=40, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=40, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dayaheadtotalloadforecast',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('totalloadvalue', models.DecimalField(db_column='TotalLoadValue', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
                ('areacodeid', models.ForeignKey(db_column='AreaCodeId', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Allocatedeicdetail')),
                ('areatypecodeid', models.ForeignKey(blank=True, db_column='AreaTypeCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Areatypecode')),
                ('mapcodeid', models.ForeignKey(blank=True, db_column='MapCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mapcode')),
                ('resolutioncodeid', models.ForeignKey(blank=True, db_column='ResolutionCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Resolutioncode')),
            ],
            options={
                'db_table': 'dayaheadtotalloadforecast',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Aggregatedgenerationpertype',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('actualgenerationoutput', models.DecimalField(db_column='ActualGenerationOutput', decimal_places=2, max_digits=24)),
                ('actualconsuption', models.DecimalField(db_column='ActualConsuption', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
                ('areacodeid', models.ForeignKey(db_column='AreaCodeId', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Allocatedeicdetail')),
                ('areatypecodeid', models.ForeignKey(blank=True, db_column='AreaTypeCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Areatypecode')),
                ('mapcodeid', models.ForeignKey(blank=True, db_column='MapCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mapcode')),
                ('productiontypeid', models.ForeignKey(blank=True, db_column='ProductionTypeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Productiontype')),
                ('resolutioncodeid', models.ForeignKey(blank=True, db_column='ResolutionCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Resolutioncode')),
            ],
            options={
                'db_table': 'aggregatedgenerationpertype',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Actualtotalload',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('entitycreatedat', models.DateTimeField(db_column='EntityCreatedAt')),
                ('entitymodifiedat', models.DateTimeField(db_column='EntityModifiedAt')),
                ('actiontaskid', models.BigIntegerField(db_column='ActionTaskID')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=2, null=True)),
                ('year', models.IntegerField(db_column='Year')),
                ('month', models.IntegerField(db_column='Month')),
                ('day', models.IntegerField(db_column='Day')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('areaname', models.CharField(blank=True, db_column='AreaName', max_length=200, null=True)),
                ('updatetime', models.DateTimeField(db_column='UpdateTime')),
                ('totalloadvalue', models.DecimalField(db_column='TotalLoadValue', decimal_places=2, max_digits=24)),
                ('rowhash', models.CharField(blank=True, db_column='RowHash', max_length=255, null=True)),
                ('areacodeid', models.ForeignKey(db_column='AreaCodeId', on_delete=django.db.models.deletion.DO_NOTHING, to='api.Allocatedeicdetail')),
                ('areatypecodeid', models.ForeignKey(blank=True, db_column='AreaTypeCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Areatypecode')),
                ('mapcodeid', models.ForeignKey(blank=True, db_column='MapCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Mapcode')),
                ('resolutioncodeid', models.ForeignKey(blank=True, db_column='ResolutionCodeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.Resolutioncode')),
            ],
            options={
                'db_table': 'actualtotalload',
                'managed': True,
            },
        ),
    ]
