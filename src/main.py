from utils import block_to_block_type


def main():
    markdown_text = """> Hed\n xd"""    
    blocks = block_to_block_type(markdown_text)
    print(blocks)

main()
