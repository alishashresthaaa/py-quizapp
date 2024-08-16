import json
from django.core.management.base import BaseCommand
import argparse
from typing import Any, Dict, List, TypedDict

class AnswerDict(TypedDict):
    answer_text: str
    is_correct: bool

class QuestionDict(TypedDict):
    question_text: str
    category: str
    answers: List[AnswerDict]

class Command(BaseCommand):
    help = 'Load questions from a JSON file'

    def add_arguments(self, parser: argparse.ArgumentParser) -> None:
        parser.add_argument('json_file', type=str, help='The JSON file containing questions and answers')

    def handle(self, *args: Any, **kwargs: Dict[str, Any]) -> None:
        from core.models import Answer, Question, Category  # Move import here

        json_file = kwargs['json_file']
        
        try:
            with open(json_file, 'r') as file:
                data: List[QuestionDict] = json.load(file)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File {json_file} not found'))
            return
        except json.JSONDecodeError:
            self.stderr.write(self.style.ERROR(f'Error decoding JSON from file {json_file}'))
            return
        
        for item in data:
            question_text = item['question_text']
            category_name = item['category']
            
            # Get or create the category
            category, created = Category.objects.get_or_create(name=category_name)
            
            question = Question.objects.create(question_text=question_text, category=category)
            
            for answer in item['answers']:
                Answer.objects.create(
                    question=question,
                    answer_text=answer['answer_text'],
                    is_correct=answer['is_correct']
                )
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded questions from JSON file'))