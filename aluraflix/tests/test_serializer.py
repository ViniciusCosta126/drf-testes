from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class TestCaseProgramaSerializer(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo='Procurando ninguem em latim',
            data_lancamento='2003-07-04',
            tipo='F',
            likes=2340,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_os_campos_que_estao_sendo_serializados(self):
        '''Teste que verifica os campos que estao sendo serializados'''

        data = self.serializer.data

        self.assertEqual(set(data.keys()), set(
            ['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudos_dos_campos_serializaos(self):
        '''Verifica o conteudo dos campos serializados'''
        data = self.serializer.data

        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['data_lancamento'],
                         self.programa.data_lancamento)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['likes'], self.programa.likes)
