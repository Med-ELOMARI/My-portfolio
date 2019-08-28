# -*- encoding: utf-8 -*-
"""
Fully Coded App by AppSeed.us
License: commercial
Read more at https://appseed.us/pricing
Copyright (c) 2019 - present AppSeed.us
"""

import os
from app import app
from app import db

#----------------------------------------
# launch
#----------------------------------------

if __name__ == "__main__":
	db.create_all()

	port = int(os.environ.get("PORT", 5000))
	app.run(port=port, debug=True)
	#app.run(ssl_context='adhoc')

    