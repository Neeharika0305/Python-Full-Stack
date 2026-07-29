{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2fdea5a6-f72f-416e-a266-9b88636f37b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "200\n"
     ]
    }
   ],
   "source": [
    "import importlib\n",
    "import modules\n",
    "\n",
    "importlib.reload(modules)\n",
    "\n",
    "print(modules.add(10, 20))\n",
    "print(modules.multiply(10, 20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "31e63baa-5d74-4c93-975e-b3cfe8106a55",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "from modules import add\n",
    "print(add(10,20))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0d89f972-c38d-4ede-a6c5-a4d69a2645c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n",
      "600\n"
     ]
    }
   ],
   "source": [
    "# to import all modules\n",
    "\n",
    "from modules import *\n",
    "\n",
    "print(add(10,20))\n",
    "print(multiply(20,30))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b1591846-055d-4b10-9fe4-280e3fe01a6c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.141592653589793\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "print(math.pi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d52c9bbc-8d0f-45fa-a7a5-615f42aa8075",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<built-in function getcwd>\n",
      "<built-in function listdir>\n",
      "['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'multiply']\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "print(os.getcwd)\n",
    "print(os.listdir)\n",
    "print(dir(modules))\n",
    "print(os.mkdir('new folder'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b1398c9-d65e-40bf-b7c2-66744794fc22",
   "metadata": {},
   "outputs": [],
   "source": [
    "getdnb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "fb35dfa5-5698-415c-842e-59de4b7fb83b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2026 7 29\n",
      "14 : 40 : 21 \n",
      "2026-07-29\n",
      "2026-08-01\n",
      "-575 days, 9:19:38.286519\n"
     ]
    }
   ],
   "source": [
    "from datetime import datetime, date, timedelta\n",
    "now = datetime.now()\n",
    "print(now.year,now.month,now.day)\n",
    "print(now.strftime('%H : %M : %S '))\n",
    "today = date.today()\n",
    "print(today)\n",
    "\n",
    "tomorrow = today + timedelta(days = 3)\n",
    "print(tomorrow)\n",
    "\n",
    "diff = datetime(2025,1,1) - datetime.now()\n",
    "print(diff)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
