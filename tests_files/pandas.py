# total_height = men_menu.size["height"]
            # driver.set_window_size(1920, total_height)
# driver.save_screenshot('images/' + str(i) + "--page_img.png")  # save screenshot
            # img = Image.open('images/' + str(i) + "--page_img.png")  # open image(screenshot)
            # custom_config = r'-c preserve_interword_spaces=1 --oem 1 --psm 1 -l eng'
            # image_text = pytesseract.image_to_data(img, config=custom_config, output_type=Output.DICT)
            # df = pd.DataFrame(image_text)
            # df1 = df[(df.conf != '-1') & (df.text != ' ') & (df.text != '')]  # clean up blanks
            # sorted_blocks = df1.groupby('block_num').first().sort_values('top').index.tolist()  # sort blocks vertically
            # for block in sorted_blocks:
            #     curr = df1[df1['block_num'] == block]
            #     sel = curr[curr.text.str.len() > 3]
            #     char_w = (sel.width / sel.text.str.len()).mean()
            #     prev_par, prev_line, prev_left = 0, 0, 0
            #     text = ''
            #     for ix, ln in curr.iterrows():
            #         if prev_par != ln['par_num']:
            #             text += '\n'  # add new line when necessary
            #             prev_par = ln['par_num']
            #             prev_line = ln['line_num']
            #             prev_left = 0
            #         elif prev_line != ln['line_num']:
            #             text += '\n'
            #             prev_line = ln['line_num']
            #             prev_left = 0
            #
            #         added = 0  # num of spaces that should be added
            #         if ln['left'] / char_w > prev_left + 1:
            #             added = int((ln['left']) / char_w) - prev_left
            #             # spaces_to_add = added - 70
            #             text += ' ' * added
            #         text += ln['text'] + ' '
            #         prev_left += len(ln['text']) + added + 1
            #     text += '\n'




# if 'def ' in text and ':' in text:

    #     # text_for_each_page += text
    #     # text_for_each_page += '\n'
    #     # text_to_be_summarized += text
    #     key_name = re.search(r'(?<=def)(.*)(?=\:)', text)


# func_name = ''
    # print(str(len(text_la)), text_la)