from django.shortcuts import render, redirect
from django.views import View

import pickle
import numpy as np


class Recommender(View):

    with open('popular.pkl', 'rb') as f:
        data = pickle.load(f)

    with open('pt.pkl', 'rb') as f:
        data2 = pickle.load(f)

    with open('books.pkl', 'rb') as f:
        data3 = pickle.load(f)

    with open('similarity_scores.pkl', 'rb') as f:
        data4 = pickle.load(f)


    @staticmethod
    def get(self, request, book_name=None, votes=None, rating=None):
        with open('popular.pkl', 'rb') as f:
            data = pickle.load(f)
        info = { book_name : list(data['Book-Title'].values),
                author : list(data['Book-Author'].values),
                image : list(data['Image-URL-M'].values),
                votes : list(data['num_ratings'].values),
                rating : list(data['avg_ratings'].values),
        }
        return render(request, 'index-recommender.html', info)

    @staticmethod
    def post(self, request, data2=None, data4=None, data3=None):
        user_input = request.form.get('user_input')
        index = np.where(data2.index == user_input)[0][0]
        similar_items = sorted(list(enumerate(data4[index])), key=lambda x: x[1], reverse=True)[1:5]

        dataf = []
        for i in similar_items:
            item = []
            temp_df = data3[data3'Book-Title'] == data2.index[i[0]],
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values)),
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values)),
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values)),

            dataf.append(item),

        print(dataf)

        return render(request, 'recommend.html', dataf)


