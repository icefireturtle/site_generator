import unittest
from blocktype import BlockType, block_to_block_type
from split_nodes import markdown_to_blocks

class TestBlockType(unittest.TestCase):
    def test_paragraph_block_to_blocktype(self):
        type = BlockType.PARAGRAPH
        block = "This is a paragraph"
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)
        

    def test_single_heading_block_to_blocktype(self):
        type = BlockType.HEADING
        block = "# This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_multi_heading_block_to_blocktype(self):
        type = BlockType.HEADING
        block = "### This is a heading with multiple #'s"
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_code_block_to_blocktype(self):
        type = BlockType.CODE
        block = """```\nThis is a code block with some code\n```"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_quote_no_space_lead_block_to_blocktype(self):
        type = BlockType.QUOTE
        block = """>no leading spaces\n>four score\n>and three years\n>ago"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_quote_no_space_lead_block_to_blocktype(self):
        type = BlockType.QUOTE
        block = """> this has a\n> leading space\n> in each"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_unordered_list_block_to_blocktype(self):
        type = BlockType.UNORDERED_LIST
        block = """- this\n- is\n- an \n- unordered\n- list"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_paragraph_not_unordered_list_block_to_blocktype(self):
        type = BlockType.PARAGRAPH
        block = """- this\n- is\n-NOT\n- an\n- unordered\n- list"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_orderd_list_block_to_blocktype(self):
        type = BlockType.ORDERED_LIST
        block = """1. this\n2. is\n3. an\n4. ordered\n5. list"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)

    def test_paragraph_not_orderd_list_block_to_blocktype(self):
        type = BlockType.PARAGRAPH
        block = """1. this\n2. is\nNOT\n3. an\n4. ordered\n5. list"""
        block_type = block_to_block_type(block)
        self.assertEqual(type, block_type)


    def test_multi_block_to_blocktype(self):
        types = []
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        for block in blocks:
            type = block_to_block_type(block)
            types.append(type)
        self.assertListEqual(
            types,
            [
                BlockType.PARAGRAPH, 
                BlockType.PARAGRAPH, 
                BlockType.UNORDERED_LIST
            ]
        )

    
