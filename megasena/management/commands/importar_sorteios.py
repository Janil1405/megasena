import requests
from django.core.management.base import BaseCommand
from megasena.models import Sorteio
from datetime import datetime

class Command(BaseCommand):
    help = 'Importa os sorteios da Mega-Sena de 2024'

    def handle(self, *args, **kwargs):
        url = "https://loteriascaixa-api.herokuapp.com/api/megasena"
        page = 1  # Iniciar na primeira página
        sorteios_importados = 0
        
        while True:
            # Fazer a requisição para a página atual
            response = requests.get(f"{url}?page={page}")
            
            # Verificar se a requisição foi bem-sucedida
            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f"Erro ao acessar a API: {response.status_code}"))
                return

            # Obter os dados da resposta JSON
            data = response.json()

            # Verificar se não há dados retornados (caso tenhamos chegado ao fim)
            if not data:
                break

            for sorteio in data:
                # Verificar se o sorteio é de 2024
                data_sorteio = datetime.strptime(sorteio['data'], '%d/%m/%Y').date()
                if data_sorteio.year != 2024:
                    continue  # Ignorar sorteios de anos diferentes de 2024

                # Verificar se a chave 'dezenas' existe no dicionário
                if 'dezenas' not in sorteio:
                    self.stdout.write(self.style.ERROR(f"A chave 'dezenas' não foi encontrada no sorteio de {sorteio['data']}"))
                    continue

                # Converter a lista de dezenas para uma string separada por vírgulas
                numeros = ', '.join(sorteio['dezenas'])

                # Salvar o sorteio no banco de dados
                Sorteio.objects.create(data=data_sorteio, numeros=numeros)
                sorteios_importados += 1

            # Se não houver próxima página, parar o loop
            page += 1  # Passar para a próxima página

        self.stdout.write(self.style.SUCCESS(f'{sorteios_importados} sorteios de 2024 importados com sucesso!'))
