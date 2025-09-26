#####################################################################
# Copyright 2022 Arun Madhu www.arunmadhu.com . All Rights Reserved.
# Owner       :  Arun Madhu
# Created Date:  22/07/2022
# Updater     :  Arun Madhu
# Updated Date:  24/07/2022
#####################################################################

import xlwt


# This style will be applied to worksheet head row.
style_head_row = xlwt.easyxf("""    
    align:
      wrap False,
      vert center,
      horiz center;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    font:
      name Calibri,
      colour_index white,
      bold on,
      height 320;
    pattern:
      pattern solid,
      fore-colour 0x11;
    """
  )

  # Define worksheet data row style. 
style_data_row = xlwt.easyxf("""
    align:
      wrap False,
      vert center,
      horiz left;
    font:
      name Calibri,
      bold off,
      height 300;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    """
  )
    # Define worksheet data row style. 
style_QTY_row = xlwt.easyxf("""

    align:
      wrap False,
      vert center,
      horiz center;
    font:
      name Calibri,
      bold off,
      height 300;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    """
  )

need_QTY_row = xlwt.easyxf("""

    align:
      wrap False,
      vert center,
      horiz center;
    font:
      name Calibri,
      bold off,
      height 300;
    borders:
      left THIN,
      right THIN,
      top THIN,
      bottom THIN;
    pattern:
      pattern solid,
      fore-colour red;
    """
  )
font = xlwt.Font()
font.name = 'Calibri'
font.height = 300
alignment = xlwt.Alignment()
alignment.horz = alignment.HORZ_CENTER
alignment.vert = alignment.VERT_CENTER
borders = xlwt.Borders()
borders.left = 1
borders.right = 1
borders.top = 1
borders.bottom = 1
date_style = xlwt.XFStyle()
date_style.alignment = alignment
date_style.font = font
date_style.num_format_str = 'dd-mmm-yyyy'
date_style.borders = borders
       
     
# Default Cell Width
col_width = 256 * 20
# Create your views here.
     
     