from marshmallow_jsonschema.base import dump_schema

from . import BaseTest, UserSchema


class TestDumpSchema(BaseTest):

    def test_dump_schema(self):
        schema = UserSchema()
        dumped = dump_schema(schema)
        self.assertGreater(len(schema.fields), 1)
        for field_name, field in schema.fields.items():
            self.assertIn(field_name, dumped['properties'])
