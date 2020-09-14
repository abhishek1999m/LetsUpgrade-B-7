#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pylint


# In[4]:


get_ipython().run_cell_magic('writefile', 'test_prime.py', '\n"""Let the prime list be empty at first."""\n\nprimes = []\n\nfor possiblePrime in range(2, 200):\n    ISPRIME = True\n    for num in range(2, possiblePrime):\n        if possiblePrime % num == 0:\n            ISPRIME = False\n    if ISPRIME:\n        primes.append(possiblePrime)\n\nprint(primes)')


# In[11]:


get_ipython().system(' pylint "test_prime.py"')


# In[12]:


get_ipython().run_cell_magic('writefile', 'we_test_prime.py', '\n"""This function tests whether a number is prime or not."""\ndef is_prime(number):\n    """Return True if number is prime."""\n    for i in range(number):\n        if number % i == 0:\n            return False\n\n    return True')


# In[13]:


get_ipython().system(' pylint "we_test_prime.py"')


# In[54]:


get_ipython().run_cell_magic('writefile', 'final_test_prime.py', '"""This is final test whether a number is prime or not."""\nimport unittest\nimport we_test_prime\n\nclass PrimesTestCase(unittest.TestCase):\n    """Tests for `primes.py`."""\n\n    def test_is_five_prime(self):\n        """Is five successfully determined to be prime?"""\n        result = we_test_prime.is_prime(5)\n        self.assertTrue(result, True)\n    def test_other_prime(self):\n        """Is other no. successfully determined to be prime?"""\n        result = we_test_prime.is_prime(6)\n        self.assertTrue(result, True)\n\nif __name__ == \'__main__\':\n    unittest.main()')


# In[55]:


get_ipython().system(' pylint "final_test_prime.py"')


# ### Generator Assignment

# In[36]:


def armstrong():
    for i in range(1,1000):
        order=len(str(i))
        sum=0
        temp=i
        while temp>0:
            digit=temp%10
            sum+=digit**order
            temp//=10
        if i==sum:
            yield i
            


# In[37]:


list(armstrong())

