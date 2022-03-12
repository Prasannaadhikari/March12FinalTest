#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


df  = pd.read_csv('intelligentGuessingDataSet.csv', encoding='latin-1')


# In[8]:


df.head(10)


# In[14]:


df.rename(columns={'Email Pattern':'Output'}, inplace=True)


# In[15]:


df.drop(columns={'Comments'}, inplace=True)


# In[23]:


X=df[:20]


# In[25]:


Y=df[21:]


# In[54]:


for email in Y['email']:
    if '.' in email:
            esplit = email.split(".")
            Y['firstname'] = ''.join(e for e in Y['firstname'] if e.isalnum())
            if Y['firstname'] == emsplit[0] and Y['lastname'] == esplit[1] or Y['firstname' == '' and Y['lastname'] == esplit[1]:
    


# In[40]:


# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
# from sklearn.linear_model import SGDClassifier
# from sklearn.model_selection import GridSearchCV
# from sklearn.pipeline import Pipeline


# In[29]:


# vectorizer = CountVectorizer()


# In[39]:


# out = vectorizer.fit_transform(df['email'])


# In[41]:


# pipeline = Pipeline(
#     [
#         ("vect", CountVectorizer()),
#         ("tfidf", TfidfTransformer()),
#         ("clf", SGDClassifier()),
#     ]
# )


# In[42]:


# parameters = {
#     "vect__max_df": (0.5, 0.75, 1.0),
#     "vect__ngram_range": ((1, 1), (1, 2)), 
#     "clf__max_iter": (20,),
#     "clf__alpha": (0.00001, 0.000001),
#     "clf__penalty": ("l2", "elasticnet"),
# }


# In[43]:


# grid_search = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)


# In[47]:


# grid_search.fit(X['email'], X['Output'])


# In[ ]:


df.to_csv("problemset1_submission.csv", index=False)

