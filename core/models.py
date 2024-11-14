from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from stdimage.models import StdImageField

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ser is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ser is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    TIPO_CHOICES = [
        ('FUNC_V2', 'Funcionário V2'),
        ('FUNC_VV', 'Funcionário VV'),
        ('CLI_V2', 'Cliente V2'),
        ('DEV', 'Desenvolvimento'),
    ]
    perfil = StdImageField(
        upload_to='perfil/',
        delete_orphans=True,
        blank=True,
        variations={'thumb': {'width': 50, 'height': 50, 'crop': True}}
    )
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='DEV')
    email = models.EmailField('E-mail', unique=True)
    is_staff = models.BooleanField('Membros da Equipe', default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.first_name
    
    objects = UserManager()


class Municipio(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.CharField(max_length=2)  # Código de estado de 2 caracteres

    def __str__(self):
        return self.nome


class Propriedade(models.Model):
    nome = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=100)
    ccir = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.nome


class Titular(models.Model):
    cpf = models.CharField(max_length=11, unique=True)
    rg = models.CharField(max_length=20)
    nome = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=100)
    naturalidade = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class CNPJ(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    razao_social = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return self.razao_social


class Proprietario(models.Model):
    TIPO_PROPRIETARIO_CHOICES = [
        ('titular', 'Titular'),
        ('cnpj', 'CNPJ'),
    ]

    tipo = models.CharField(max_length=10, choices=TIPO_PROPRIETARIO_CHOICES)
    cpf = models.OneToOneField(Titular, on_delete=models.CASCADE, blank=True, null=True)
    cnpj = models.OneToOneField(CNPJ, on_delete=models.CASCADE, blank=True, null=True)
    representante = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.cpf or self.cnpj)


class ProprietarioPropriedade(models.Model):
    propriedade = models.ForeignKey(Propriedade, on_delete=models.CASCADE)
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.propriedade.nome} - {self.proprietario}"
