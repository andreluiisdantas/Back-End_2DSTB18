import pandas as pd
from django.core.management.base import BaseCommand
from django.db import transaction
from api.models import Livro, Autor, Editora


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="Population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *args, **options):
        df = pd.read_csv(options["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]

        if options["truncate"]:
            Livro.objects.all().delete()
            Editora.objects.all().delete()

        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()
        df["autor"] = df["autor"].astype(str).str.strip()
        df["editor"] = df["editor"].astype(str).str.strip()
        df["isbn"] = df["isbn"].astype(str).str.strip()
        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["dimensoes"] = df["dimensoes"].astype(str).str.strip()

        df = df.query("titulo != '' and subtitulo != ''")

        criados = atualizados = ignorados = 0

        for row in df.itertuples(index=False):
            nome_completo = row.autor.strip()
            partes = nome_completo.split(" ", 1)
            nome = partes[0]
            sobrenome = partes[1] if len(partes) > 1 else ""

            autor_obj = Autor.objects.filter(nome=nome, sobrenome=sobrenome).first()
            if not autor_obj:
                ignorados += 1
                continue

            editora_obj, _ = Editora.objects.get_or_create(editora=row.editor)

            livro, created = Livro.objects.update_or_create(
                titulo=row.titulo,
                subtitulo=row.subtitulo,
                autor=autor_obj,
                editor=editora_obj,
                defaults={
                    "isbn": row.isbn,
                    "descricao": row.descricao,
                    "idioma": row.idioma,
                    "ano_publicacao": row.ano_publicacao,
                    "paginas": row.paginas,
                    "preco": row.preco,
                    "estoque": row.estoque,
                    "desconto": row.desconto,
                    "disponivel": str(row.disponivel).lower() in ["true", "1"],
                    "dimensoes": row.dimensoes,
                    "peso": row.peso,
                }
            )

            criados += int(created)
            atualizados += int(not created)

        self.stdout.write(self.style.SUCCESS(
            f"Criados: {criados}\nAtualizados: {atualizados}\nIgnorados (autor não encontrado): {ignorados}"
        ))
