from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)  # E-mail único
    senha = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'usuarios'

class Onibus(models.Model):  # Definindo a classe Onibus fora da classe Usuario
    id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20)
    capacidade = models.IntegerField()

    def __str__(self):
        return self.numero

    class Meta:
        db_table = 'onibus'

class LocalizacaoOnibus(models.Model):  # Definindo a classe LocalizacaoOnibus fora da classe Usuario
    id = models.AutoField(primary_key=True)
    onibus = models.ForeignKey(Onibus, on_delete=models.CASCADE)  # Relacionamento com 'Onibus'
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Ônibus {self.onibus.numero} - {self.latitude}, {self.longitude}'

    class Meta:
        db_table = 'localizacao_onibus'