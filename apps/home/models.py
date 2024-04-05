# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import datetime, os, string
# from payment.models import Payment


class Accountbilling(models.Model):
    billingid = models.AutoField(db_column='billingID', primary_key=True)  # Field name made lowercase.
    studentid = models.CharField(db_column='studentID', max_length=255)  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.
    termid = models.IntegerField(db_column='TermID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountbilling'


class Accountdetails(models.Model):
    acctdid = models.AutoField(db_column='acctdID', primary_key=True)  # Field name made lowercase.
    billingid = models.IntegerField(db_column='billingID')  # Field name made lowercase.
    acctid = models.IntegerField(db_column='acctID')  # Field name made lowercase.
    discountid = models.IntegerField(db_column='DiscountID')  # Field name made lowercase.
    amountpay = models.FloatField(db_column='AmountPay')  # Field name made lowercase.
    datetransaction = models.CharField(db_column='DateTransaction', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountdetails'


class Accountdiscount(models.Model):
    acctdisid = models.AutoField(db_column='acctdisID', primary_key=True)  # Field name made lowercase.
    billingid = models.IntegerField(db_column='billingID')  # Field name made lowercase.
    discountid = models.IntegerField(db_column='DiscountID')  # Field name made lowercase.
    acctid = models.IntegerField(db_column='acctID', blank=True, null=True)  # Field name made lowercase.
    datetransaction = models.CharField(db_column='DateTransaction', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountdiscount'


class Accountitem(models.Model):
    acctid = models.AutoField(db_column='acctID', primary_key=True)  # Field name made lowercase.
    accttitle = models.CharField(db_column='AcctTitle', max_length=255)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountitem'


class Accountpayment(models.Model):
    paymentid = models.AutoField(db_column='paymentID', primary_key=True)  # Field name made lowercase.
    billingid = models.IntegerField(db_column='billingID')  # Field name made lowercase.
    transactionno = models.IntegerField(db_column='TransactionNo')  # Field name made lowercase.
    payfor = models.CharField(db_column='PayFor', max_length=255)  # Field name made lowercase.
    mop = models.CharField(db_column='MOP', max_length=255)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    amountpay = models.FloatField(db_column='AmountPay')  # Field name made lowercase.
    amountchange = models.FloatField(db_column='AmountChange')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=255)  # Field name made lowercase.
    ornumber = models.CharField(db_column='ORNumber', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    transactiondate = models.CharField(db_column='TransactionDate', max_length=255)  # Field name made lowercase.
    systemtransactiondate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accountpayment'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categoryfee(models.Model):
    categoryid = models.AutoField(db_column='categoryID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categoryfee'


class Citizenship(models.Model):
    citizenshipid = models.AutoField(db_column='CitizenshipID', primary_key=True)  # Field name made lowercase.
    citizenship = models.CharField(db_column='Citizenship', max_length=255, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'citizenship'


class Clocking(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING, db_column='student')
    inam = models.CharField(db_column='inAM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    outam = models.CharField(db_column='outAM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inpm = models.CharField(db_column='inPM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    outpm = models.CharField(db_column='outPM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='date',  max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clocking'


class Customerinfo(models.Model):
    custid = models.CharField(db_column='CustID', unique=True, max_length=255)  # Field name made lowercase.
    cusname = models.CharField(db_column='CusName', max_length=255)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customerinfo'


class Defective(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty')  # Field name made lowercase.
    remarks = models.CharField(db_column='Remarks', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'defective'


class Departments(models.Model):
    deptid = models.AutoField(db_column='DeptID', primary_key=True)  # Field name made lowercase.
    department = models.CharField(db_column='Department', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'departments'


class Discount(models.Model):
    discountid = models.AutoField(db_column='DiscountID', primary_key=True)  # Field name made lowercase.
    discountname = models.CharField(db_column='DiscountName', max_length=255)  # Field name made lowercase.
    amount = models.FloatField(db_column='Amount')  # Field name made lowercase.
    percentage = models.CharField(db_column='Percentage', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discount'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EntryMonitoring(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING)
    clockin = models.CharField(max_length=50, blank=True, null=True)
    clockout = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(null=False)


class Feestructure(models.Model):
    structureid = models.AutoField(db_column='structureID', primary_key=True)  # Field name made lowercase.
    structurename = models.CharField(db_column='structureName', max_length=250, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feestructure'


class Gradelevel(models.Model):
    gradelevel_id = models.AutoField(db_column='GradeLevel_ID', primary_key=True)  # Field name made lowercase.
    gradelevel = models.CharField(db_column='GradeLevel', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gradelevel'


class Gradelevelsection(models.Model):
    glsid = models.AutoField(db_column='glsID', primary_key=True)  # Field name made lowercase.
    gradelevel_id = models.IntegerField(db_column='GradeLevel_ID')  # Field name made lowercase.
    sectionid = models.IntegerField(db_column='SectionID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gradelevelsection'


class Gsacademicyear(models.Model):
    gacademicyearid = models.AutoField(db_column='GAcademicYearID', primary_key=True)  # Field name made lowercase.
    year1 = models.CharField(db_column='Year1', max_length=100)  # Field name made lowercase.
    year2 = models.CharField(db_column='Year2', max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gsacademicyear'


class Gsubjects(models.Model):
    gsubjectid = models.AutoField(db_column='GSubjectID', primary_key=True)  # Field name made lowercase.
    subjectcode = models.CharField(db_column='SubjectCode', max_length=255)  # Field name made lowercase.
    subject = models.CharField(db_column='Subject', max_length=255)  # Field name made lowercase.
    gradelevel_id = models.IntegerField(db_column='GradeLevel_ID')  # Field name made lowercase.
    schedule = models.CharField(db_column='Schedule', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=255)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gsubjects'


class Itemfilemaintenance(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=255)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=255)  # Field name made lowercase.
    itembrand = models.CharField(db_column='ItemBrand', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemfilemaintenance'


class Itemtrackrecord(models.Model):
    itrid = models.AutoField(db_column='ITRID', primary_key=True)  # Field name made lowercase.
    custid = models.CharField(db_column='CustID', max_length=255)  # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    datetrack = models.DateTimeField(db_column='DateTrack')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'itemtrackrecord'


class Jhstudentrecord(models.Model):
    srid = models.AutoField(db_column='SRID', primary_key=True)  # Field name made lowercase.
    registerid = models.IntegerField(db_column='RegisterID')  # Field name made lowercase.
    studentid = models.CharField(db_column='StudentID', max_length=255)  # Field name made lowercase.
    gradelevel_id = models.IntegerField(db_column='GradeLevel_ID')  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    session = models.CharField(db_column='Session', max_length=255)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255)  # Field name made lowercase.
    daterecord = models.CharField(db_column='DateRecord', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jhstudentrecord'


class LmsAllbooks(models.Model):
    book_id = models.AutoField(primary_key=True)
    class_id = models.IntegerField()
    catid = models.IntegerField(db_column='catID')  # Field name made lowercase.
    book_title = models.CharField(max_length=255)
    callno = models.CharField(db_column='callNo', max_length=255)  # Field name made lowercase.
    author = models.CharField(max_length=255)
    datepublish = models.CharField(max_length=255)
    availability = models.CharField(max_length=255)
    dateadded = models.DateTimeField(db_column='dateAdded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_allbooks'


class LmsBookcategory(models.Model):
    cat_id = models.AutoField(primary_key=True)
    bookcategory = models.CharField(db_column='bookCategory', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_bookcategory'


class LmsBorrow(models.Model):
    brid = models.AutoField(db_column='BRID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.CharField(max_length=255)
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datetrack = models.DateTimeField(db_column='dateTrack')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_borrow'


class LmsBorrowreturn(models.Model):
    brid = models.AutoField(db_column='BRID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.IntegerField()
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    returndateuntil = models.CharField(db_column='returnDateUntil', max_length=255)  # Field name made lowercase.
    dateborrow = models.CharField(db_column='dateBorrow', max_length=255)  # Field name made lowercase.
    datereturn = models.CharField(db_column='dateReturn', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_borrowreturn'


class LmsCategory(models.Model):
    catid = models.AutoField(db_column='catID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(db_column='Category', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_category'


class LmsClassification(models.Model):
    class_id = models.AutoField(primary_key=True)
    bookclassification = models.CharField(db_column='bookClassification', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_classification'


class LmsFinefees(models.Model):
    fine_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255)
    penalty = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lms_finefees'


class LmsLogs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    lrn_no = models.IntegerField()
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datetrack = models.DateTimeField(db_column='dateTrack')  # Field name made lowercase.
    dateuntil = models.CharField(db_column='dateUntil', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_logs'


class LmsReturn(models.Model):
    brid = models.IntegerField(db_column='BRID')  # Field name made lowercase.
    lrn_no = models.CharField(max_length=255)
    book_id = models.IntegerField()
    status = models.CharField(max_length=255)
    datereturn = models.DateTimeField(db_column='dateReturn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lms_return'


class LmsStudentrecord(models.Model):
    lrn_no = models.CharField(unique=True, max_length=255)
    studentname = models.CharField(db_column='studentName', max_length=255)  # Field name made lowercase.
    grade = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lms_studentrecord'


class Logs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=100)  # Field name made lowercase.
    marks = models.CharField(db_column='Marks', max_length=255, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.
    dateop = models.DateTimeField(db_column='DateOp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logs'


class Managestrand(models.Model):
    strandid = models.AutoField(db_column='strandID', primary_key=True)  # Field name made lowercase.
    strandcode = models.CharField(db_column='StrandCode', max_length=255)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managestrand'


class Packagelist(models.Model):
    packlistid = models.AutoField(db_column='packlistID', primary_key=True)  # Field name made lowercase.
    packageid = models.IntegerField(db_column='packageID')  # Field name made lowercase.
    acctid = models.IntegerField(db_column='acctID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packagelist'


class Packages(models.Model):
    packageid = models.AutoField(db_column='packageID', primary_key=True)  # Field name made lowercase.
    packagetitle = models.CharField(db_column='PackageTitle', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'packages'


class Parent(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    middlename = models.CharField(max_length=20, blank=True, null=True)
    lastname = models.CharField(max_length=20, blank=True, null=True)
    dateofbirth = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    dateregistered = models.DateField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=45, blank=True, null=True)
    mystatus = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent'


class ParentMystudent(models.Model):
    parent = models.ForeignKey(Parent, models.DO_NOTHING, db_column='parent', blank=True, null=True)
    mystudent = models.ForeignKey('Student', models.DO_NOTHING, db_column='mystudent', blank=True, null=True)
    status = models.CharField(db_column='status', max_length=20, null=True)

    class Meta:
        managed = False
        db_table = 'parent_mystudent'


class PaymentUpload(models.Model):
    idupload = models.AutoField(db_column='idupload', primary_key=True)
    image = models.ImageField(db_column='image', upload_to='media/', null=True)
    description = models.CharField(db_column='description', max_length=50, null=True)

    class Meta:
        managed = True
        db_table = 'payment_upload'


class Paymentmethod(models.Model):
    pmtdid = models.AutoField(db_column='pmtdID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentmethod'



class Pmslogs(models.Model):
    logid = models.AutoField(db_column='LogID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=255)  # Field name made lowercase.
    marks = models.CharField(db_column='Marks', max_length=255)  # Field name made lowercase.
    dateop = models.DateTimeField(db_column='DateOp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pmslogs'


class Propertyitem(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    deptid = models.ForeignKey(Departments, models.DO_NOTHING, db_column='DeptID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.IntegerField()
    qnty = models.IntegerField(db_column='Qnty')  # Field name made lowercase.
    total_vacant = models.IntegerField(db_column='Total_Vacant')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    inventoryno = models.CharField(db_column='InventoryNo', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    dateadded = models.DateTimeField(db_column='DateAdded')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyitem'


class Propertyitemtransfer(models.Model):
    transid = models.AutoField(db_column='transID', primary_key=True)  # Field name made lowercase.
    inventoryno = models.CharField(db_column='InventoryNo', max_length=255)  # Field name made lowercase.
    currentdeptid = models.IntegerField(db_column='CurrentDeptID')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='ItemID')  # Field name made lowercase.
    itemcode = models.CharField(max_length=255)
    qnty = models.IntegerField(db_column='Qnty')  # Field name made lowercase.
    newdeptid = models.IntegerField(db_column='NewDeptID')  # Field name made lowercase.
    datetransfer = models.DateTimeField(db_column='DateTransfer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'propertyitemtransfer'


class Psstudentrecord(models.Model):
    psid = models.AutoField(db_column='psID', primary_key=True)  # Field name made lowercase.
    registerid = models.IntegerField(db_column='RegisterID')  # Field name made lowercase.
    studentid = models.CharField(db_column='StudentID', max_length=255)  # Field name made lowercase.
    gradelevel_id = models.IntegerField(db_column='GradeLevel_ID')  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    daterecord = models.CharField(db_column='DateRecord', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'psstudentrecord'


class PyrolEmpSettings(models.Model):
    pesid = models.AutoField(db_column='pesID', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(max_length=255, blank=True, null=True)
    packageid = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.CharField(max_length=255, blank=True, null=True)
    date_updated = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pyrol_emp_settings'


class PyrolEmployee(models.Model):
    peid = models.AutoField(db_column='PEid', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(max_length=255)
    empimage = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    midname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    suffix = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    martialstatus = models.CharField(max_length=255)
    nodependent = models.CharField(max_length=255)
    contactno = models.CharField(max_length=255)
    emergencyno = models.CharField(max_length=255)
    contactname = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    emailadd = models.CharField(max_length=255)
    fbacc = models.CharField(max_length=255)
    workstatus = models.CharField(max_length=2555)
    emptype = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    empstatus = models.CharField(max_length=255)
    datehired = models.CharField(max_length=255)
    dateupdate = models.CharField(max_length=255)
    taxno = models.CharField(max_length=255)
    sssno = models.CharField(max_length=255)
    pagibigno = models.CharField(max_length=255)
    philhealthno = models.CharField(max_length=255)
    gsisno = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pyrol_employee'


class PyrolEmployeetype(models.Model):
    emptyp_id = models.AutoField(db_column='emptyp_ID', primary_key=True)  # Field name made lowercase.
    emp_type = models.CharField(db_column='Emp_type', unique=True, max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pyrol_employeetype'


class PyrolPackage(models.Model):
    packagename = models.CharField(max_length=255)
    packageid = models.CharField(unique=True, max_length=255)
    employeetype = models.CharField(max_length=255)
    dateadd = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pyrol_package'


class PyrolPreparepayroll(models.Model):
    ppid = models.AutoField(db_column='PPid', primary_key=True)  # Field name made lowercase.
    payrollno = models.CharField(db_column='payrollNo', max_length=255)  # Field name made lowercase.
    payperiod = models.CharField(max_length=255)
    totalemployee = models.CharField(max_length=255)
    totalrelease = models.CharField(max_length=255)
    totalamount = models.CharField(max_length=255)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pyrol_preparepayroll'


class PyrolProcesspayroll(models.Model):
    processid = models.AutoField(db_column='processID', primary_key=True)  # Field name made lowercase.
    idno = models.CharField(db_column='idNo', max_length=255)  # Field name made lowercase.
    payrollno = models.CharField(db_column='payrollNo', max_length=255)  # Field name made lowercase.
    payperiod = models.CharField(max_length=255)
    paystatus = models.CharField(max_length=255)
    dateprocessed = models.CharField(max_length=255)
    activepackageid = models.CharField(db_column='activepackageID', max_length=255)  # Field name made lowercase.
    emptype = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    monthlyrate = models.CharField(max_length=255)
    noofdays = models.CharField(max_length=255)
    rateperday = models.CharField(max_length=255)
    totalreportdays = models.CharField(max_length=255)
    totalpaidleaves = models.CharField(max_length=255)
    totalhrslate = models.CharField(max_length=255)
    totalminslate = models.CharField(max_length=255)
    totalunpaid = models.CharField(max_length=255)
    grossincome = models.CharField(max_length=255)
    totalnetpay = models.CharField(max_length=255)
    totalot = models.CharField(db_column='totalOT', max_length=255)  # Field name made lowercase.
    honourarium = models.CharField(max_length=255)
    otherincome = models.CharField(max_length=255)
    otherincomenote = models.CharField(db_column='otherincomeNote', max_length=255)  # Field name made lowercase.
    otherincometwo = models.CharField(db_column='otherincomeTWO', max_length=255)  # Field name made lowercase.
    otherincomenotetwo = models.CharField(db_column='otherincomeNoteTWO', max_length=255)  # Field name made lowercase.
    totaladdincome = models.CharField(max_length=255)
    sss = models.CharField(max_length=255)
    pagibig = models.CharField(max_length=255)
    philhealth = models.CharField(max_length=255)
    gsis = models.CharField(max_length=255)
    deduction = models.CharField(max_length=255)
    deductionnote = models.CharField(db_column='deductionNote', max_length=255)  # Field name made lowercase.
    deductiontwo = models.CharField(db_column='deductionTWO', max_length=255)  # Field name made lowercase.
    deductionnotetwo = models.CharField(db_column='deductionNoteTWO', max_length=255)  # Field name made lowercase.
    totaldeduction = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pyrol_processpayroll'


class PyrolSettings(models.Model):
    psid = models.AutoField(db_column='PSid', primary_key=True)  # Field name made lowercase.
    empid = models.CharField(max_length=255)
    packageid = models.CharField(max_length=255, blank=True, null=True)
    typeemployee = models.CharField(max_length=255, blank=True, null=True)
    monthrate = models.FloatField(blank=True, null=True)
    nofdays = models.CharField(max_length=255, blank=True, null=True)
    ratehr = models.CharField(max_length=255, blank=True, null=True)
    rateot = models.CharField(max_length=255, blank=True, null=True)
    honourarium = models.CharField(max_length=255, blank=True, null=True)
    incomeone = models.CharField(max_length=255, blank=True, null=True)
    noteone = models.CharField(max_length=255, blank=True, null=True)
    incometwo = models.CharField(max_length=255, blank=True, null=True)
    notetwo = models.CharField(max_length=255, blank=True, null=True)
    nofleave = models.CharField(max_length=255, blank=True, null=True)
    sssemployee = models.CharField(max_length=255, blank=True, null=True)
    sssemployer = models.CharField(max_length=255, blank=True, null=True)
    pagibigemployee = models.CharField(max_length=255, blank=True, null=True)
    pagibigemployer = models.CharField(max_length=255, blank=True, null=True)
    philhlthemplyee = models.CharField(max_length=255, blank=True, null=True)
    philhlthemplyer = models.CharField(max_length=255, blank=True, null=True)
    gsisemployee = models.CharField(max_length=255, blank=True, null=True)
    gsisemployer = models.CharField(max_length=255, blank=True, null=True)
    deductone = models.CharField(max_length=255, blank=True, null=True)
    deductnote = models.CharField(max_length=255, blank=True, null=True)
    deductwo = models.CharField(max_length=255, blank=True, null=True)
    deductnotetwo = models.CharField(max_length=255, blank=True, null=True)
    paymethod = models.CharField(max_length=255, blank=True, null=True)
    bankname = models.CharField(max_length=255, blank=True, null=True)
    accountno = models.CharField(max_length=255, blank=True, null=True)
    accountname = models.CharField(max_length=255, blank=True, null=True)
    settingstatus = models.CharField(db_column='SettingStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    datecreated = models.CharField(max_length=255, blank=True, null=True)
    dateupdated = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pyrol_settings'


class RegistrationCrud(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'registration_crud'


class Religion(models.Model):
    religionid = models.AutoField(db_column='ReligionID', primary_key=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255, db_collation='utf8mb4_unicode_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'religion'


class Returnitem(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    itrid = models.ForeignKey(Itemtrackrecord, models.DO_NOTHING, db_column='ITRID')  # Field name made lowercase.
    qnty = models.IntegerField(db_column='Qnty')  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=255)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    datereturn = models.DateTimeField(db_column='DateReturn')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'returnitem'


class Sections(models.Model):
    sectionid = models.AutoField(db_column='SectionID', primary_key=True)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sections'


class Settings(models.Model):
    sid = models.AutoField(db_column='SID', primary_key=True)  # Field name made lowercase.
    newstudent = models.IntegerField(db_column='NewStudent')  # Field name made lowercase.
    enrollment = models.IntegerField(db_column='Enrollment')  # Field name made lowercase.
    payment = models.IntegerField(db_column='Payment')  # Field name made lowercase.
    rate = models.IntegerField(db_column='Rate')  # Field name made lowercase.
    downpayment = models.IntegerField(db_column='DownPayment')  # Field name made lowercase.
    subject = models.IntegerField(db_column='Subject')  # Field name made lowercase.
    adsubject = models.IntegerField(db_column='ADSubject')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'settings'


class Shstudentrecord(models.Model):
    ssrid = models.AutoField(db_column='SSRID', primary_key=True)  # Field name made lowercase.
    registerid = models.IntegerField(db_column='RegisterID')  # Field name made lowercase.
    studentid = models.CharField(db_column='StudentID', max_length=255)  # Field name made lowercase.
    gradelevel_id = models.IntegerField(db_column='GradeLevel_ID')  # Field name made lowercase.
    strandid = models.IntegerField(db_column='strandID', blank=True, null=True)  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.
    termid = models.IntegerField(db_column='TermID')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.
    session = models.CharField(db_column='Session', max_length=255)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255)  # Field name made lowercase.
    daterecord = models.CharField(db_column='DateRecord', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shstudentrecord'


class Shsubjects(models.Model):
    subjectid = models.AutoField(db_column='subjectID', primary_key=True)  # Field name made lowercase.
    category = models.CharField(max_length=100)
    subjects = models.CharField(db_column='Subjects', max_length=255)  # Field name made lowercase.
    lechr = models.IntegerField(db_column='LecHR')  # Field name made lowercase.
    labhr = models.IntegerField(db_column='labHR')  # Field name made lowercase.
    totalhr = models.IntegerField(db_column='totalHR')  # Field name made lowercase.
    rate = models.FloatField(blank=True, null=True)
    prereq = models.CharField(max_length=255)
    gradelevel = models.CharField(db_column='GradeLevel', max_length=100)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=100)  # Field name made lowercase.
    strandid = models.IntegerField(db_column='strandID')  # Field name made lowercase.
    schedule = models.CharField(db_column='Schedule', max_length=255)  # Field name made lowercase.
    time = models.CharField(db_column='Time', max_length=255)  # Field name made lowercase.
    section = models.CharField(db_column='Section', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shsubjects'


class Sidseries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    endidno = models.CharField(db_column='EndIDNo', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sidseries'


class Soa(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)  # Field name made lowercase.
    soano = models.CharField(db_column='SoaNo', max_length=20)  # Field name made lowercase.
    studentid = models.ForeignKey('Student', on_delete=models.CASCADE,  db_column='studentid', default="")
    file = models.FileField(db_column='file', upload_to='soa/', verbose_name="")  # Field name made lowercase.

    def __str__(self):
        return str(self.studentid)

    class Meta:
        managed = True
        db_table = 'soa'


class Student(models.Model):
    registerid = models.AutoField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    qrcode = models.TextField(blank=True, null=True)
    lrn = models.CharField(db_column='LRN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=255, blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathersname = models.CharField(db_column='FathersName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathersoccupation = models.CharField(db_column='FathersOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fatherscontact = models.CharField(db_column='FathersContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mothersname = models.CharField(db_column='MothersName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mothersoccupation = models.CharField(db_column='MothersOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    motherscontact = models.CharField(db_column='MothersContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardiansname = models.CharField(db_column='GuardiansName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardiansoccupation = models.CharField(db_column='GuardiansOccupation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    guardianscontact = models.CharField(db_column='GuardiansContact', max_length=255, blank=True, null=True)  # Field name made lowercase.
    curriculum = models.CharField(db_column='Curriculum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    civilstatus = models.CharField(db_column='CivilStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    juniorhigh = models.CharField(db_column='JuniorHigh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seniorhigh = models.CharField(db_column='SeniorHigh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    junioraddress = models.CharField(db_column='JuniorAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    senioraddress = models.CharField(db_column='SeniorAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    techvoccourse = models.CharField(db_column='TechvocCourse', max_length=255, blank=True, null=True)  # Field name made lowercase.
    culturalminoritygroup = models.CharField(db_column='CulturalMinorityGroup', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disabilities = models.CharField(db_column='Disabilities', max_length=255, blank=True, null=True)  # Field name made lowercase.
    birthcert = models.CharField(db_column='BirthCert', max_length=255, blank=True, null=True)  # Field name made lowercase.
    form137 = models.CharField(db_column='Form137', max_length=255, blank=True, null=True)  # Field name made lowercase.
    goodmoral = models.CharField(db_column='GoodMoral', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reportcard = models.CharField(db_column='ReportCard', max_length=255, blank=True, null=True)  # Field name made lowercase.
    esc = models.CharField(db_column='ESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    psa = models.CharField(db_column='PSA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_2x2 = models.CharField(db_column='2x2', max_length=255, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    dateregistered = models.CharField(db_column='DateRegistered', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    last_login = models.BooleanField(max_length=5, blank=False, null=False, default=0)

    def __str__(self):
        return str(self.registerid)

    class Meta:
        managed = True
        db_table = 'student'


class Studentsubjects(models.Model):
    studsubid = models.AutoField(db_column='studsubID', primary_key=True)  # Field name made lowercase.
    billingid = models.IntegerField(db_column='billingID')  # Field name made lowercase.
    gsubjectid = models.IntegerField(db_column='GSubjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentsubjects'


class StudentPrereg(models.Model):
    registerid = models.AutoField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qrcode = models.TextField(blank=True, null=True)
    studentid = models.CharField(db_column='StudentID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    studenttype = models.CharField(db_column='StudentType', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lrn = models.CharField(db_column='LRN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=50, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=50, blank=True, null=True)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathersname = models.CharField(db_column='FathersName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fathersoccupation = models.CharField(db_column='FathersOccupation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fatherscontact = models.CharField(db_column='FathersContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mothersname = models.CharField(db_column='MothersName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mothersoccupation = models.CharField(db_column='MothersOccupation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    motherscontact = models.CharField(db_column='MothersContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guardiansname = models.CharField(db_column='GuardiansName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guardiansoccupation = models.CharField(db_column='GuardiansOccupation', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guardianscontact = models.CharField(db_column='GuardiansContact', max_length=50, blank=True, null=True)  # Field name made lowercase.
    curriculum = models.CharField(db_column='Curriculum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    civilstatus = models.CharField(db_column='CivilStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    juniorhigh = models.CharField(db_column='JuniorHigh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    seniorhigh = models.CharField(db_column='SeniorHigh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    junioraddress = models.CharField(db_column='JuniorAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    senioraddress = models.CharField(db_column='SeniorAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    techvoccourse = models.CharField(db_column='TechvocCourse', max_length=50, blank=True, null=True)  # Field name made lowercase.
    culturalminoritygroup = models.CharField(db_column='CulturalMinorityGroup', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disabilities = models.CharField(db_column='Disabilities', max_length=10, blank=True, null=True)  # Field name made lowercase.
    birthcert = models.CharField(db_column='BirthCert', max_length=10, blank=True, null=True)  # Field name made lowercase.
    form137 = models.CharField(db_column='Form137', max_length=10, blank=True, null=True)  # Field name made lowercase.
    goodmoral = models.CharField(db_column='GoodMoral', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reportcard = models.CharField(db_column='ReportCard', max_length=10, blank=True, null=True)  # Field name made lowercase.
    esc = models.CharField(db_column='ESC', max_length=10, blank=True, null=True)  # Field name made lowercase.
    psa = models.CharField(db_column='PSA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    number_2x2 = models.CharField(db_column='2x2', max_length=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    dateregistered = models.DateField(db_column='DateRegistered', max_length=10, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=10, blank=True, null=True)
    reg_status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_prereg'


class Studentsubjectsh(models.Model):
    subid = models.AutoField(primary_key=True)
    billingid = models.IntegerField(db_column='billingID')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='subjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentsubjectsh'


class Teachers(models.Model):
    teacherid = models.AutoField(db_column='teacherId', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(db_column='Lastname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=250, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=255, blank=True, null=True)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=255)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    dateofbirth = models.CharField(db_column='DateOfBirth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    placeofbirth = models.CharField(db_column='PlaceOfBirth', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contactno = models.CharField(db_column='ContactNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.CharField(db_column='MaritalStatus', max_length=255, blank=True, null=True)  # Field name made lowercase.
    citizenship = models.CharField(db_column='Citizenship', max_length=255, blank=True, null=True)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    homeaddress = models.CharField(db_column='HomeAddress', max_length=255)  # Field name made lowercase.
    gacademicyearid = models.IntegerField(db_column='GAcademicYearID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachers'


class Teachersubjectjhs(models.Model):
    tsid = models.AutoField(db_column='TSID', primary_key=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='teacherId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachersubjectjhs'


class Teachersubjectshs(models.Model):
    tsid = models.AutoField(db_column='TSID', primary_key=True)  # Field name made lowercase.
    teacherid = models.IntegerField(db_column='teacherId')  # Field name made lowercase.
    subjectid = models.IntegerField(db_column='SubjectID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachersubjectshs'


class Testuser(models.Model):
    testid = models.AutoField(db_column='testID', primary_key=True)  # Field name made lowercase.
    teachersid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    qrcode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testuser'


class Totalfee(models.Model):
    totalfeeid = models.AutoField(db_column='totalFeeID', primary_key=True)  # Field name made lowercase.
    structureid = models.ForeignKey(Feestructure, models.DO_NOTHING, db_column='structureID', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categoryfee, models.DO_NOTHING, db_column='categoryID', blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'totalfee'


class Transtart(models.Model):
    transtartid = models.AutoField(db_column='transtartID', primary_key=True)  # Field name made lowercase.
    startno = models.IntegerField(db_column='StartNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'transtart'


class Users(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    username = models.CharField(unique=True, max_length=250, blank=True, null=True)
    password = models.CharField(max_length=250, blank=True, null=True)
    userrole = models.CharField(max_length=150, blank=True, null=True)
    macaddress = models.CharField(db_column='macAddress', max_length=250, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Webregistration(models.Model):
    registerid = models.AutoField(db_column='RegisterID', primary_key=True)  # Field name made lowercase.
    refno = models.CharField(db_column='RefNo', max_length=255)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=255)  # Field name made lowercase.
    suffix = models.CharField(db_column='Suffix', max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255)  # Field name made lowercase.
    birthdate = models.CharField(db_column='BirthDate', max_length=255)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=255)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255)  # Field name made lowercase.
    ethnicity = models.CharField(db_column='Ethnicity', max_length=255)  # Field name made lowercase.
    religion = models.CharField(db_column='Religion', max_length=255)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    level = models.CharField(db_column='Level', max_length=255)  # Field name made lowercase.
    strand = models.CharField(db_column='Strand', max_length=255)  # Field name made lowercase.
    fathersname = models.CharField(db_column='FathersName', max_length=255)  # Field name made lowercase.
    fathersoccupation = models.CharField(db_column='FathersOccupation', max_length=255)  # Field name made lowercase.
    fatherscontact = models.CharField(db_column='FathersContact', max_length=255)  # Field name made lowercase.
    mothersname = models.CharField(db_column='MothersName', max_length=255)  # Field name made lowercase.
    mothersoccupation = models.CharField(db_column='MothersOccupation', max_length=255)  # Field name made lowercase.
    motherscontact = models.CharField(db_column='MothersContact', max_length=255)  # Field name made lowercase.
    guardiansname = models.CharField(db_column='GuardiansName', max_length=255)  # Field name made lowercase.
    guardiansoccupation = models.CharField(db_column='GuardiansOccupation', max_length=255)  # Field name made lowercase.
    guardianscontact = models.CharField(db_column='GuardiansContact', max_length=255)  # Field name made lowercase.
    curriculum = models.CharField(db_column='Curriculum', max_length=255)  # Field name made lowercase.
    civilstatus = models.CharField(db_column='CivilStatus', max_length=255)  # Field name made lowercase.
    juniorhigh = models.CharField(db_column='JuniorHigh', max_length=255)  # Field name made lowercase.
    seniorhigh = models.CharField(db_column='SeniorHigh', max_length=255)  # Field name made lowercase.
    junioraddress = models.CharField(db_column='JuniorAddress', max_length=255)  # Field name made lowercase.
    senioraddress = models.CharField(db_column='SeniorAddress', max_length=255)  # Field name made lowercase.
    techvoccourse = models.CharField(db_column='TechvocCourse', max_length=255)  # Field name made lowercase.
    culturalminoritygroup = models.CharField(db_column='CulturalMinorityGroup', max_length=255)  # Field name made lowercase.
    disabilities = models.CharField(db_column='Disabilities', max_length=255)  # Field name made lowercase.
    birthcert = models.CharField(db_column='BirthCert', max_length=255)  # Field name made lowercase.
    form137 = models.CharField(db_column='Form137', max_length=255)  # Field name made lowercase.
    goodmoral = models.CharField(db_column='GoodMoral', max_length=255)  # Field name made lowercase.
    reportcard = models.CharField(db_column='ReportCard', max_length=255)  # Field name made lowercase.
    esc = models.CharField(db_column='ESC', max_length=255)  # Field name made lowercase.
    psa = models.CharField(db_column='PSA', max_length=255)  # Field name made lowercase.
    dateregistered = models.CharField(db_column='DateRegistered', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'webregistration'


class Wordexception(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    word = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wordexception'


class Yearterm(models.Model):
    termid = models.AutoField(db_column='TermID', primary_key=True)  # Field name made lowercase.
    term = models.CharField(db_column='Term', max_length=100, db_collation='utf8mb4_unicode_ci', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'yearterm'