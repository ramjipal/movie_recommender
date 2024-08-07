import bz2file

# Path to the original .pkl file
input_file = 'movie_recommender\similarity.pkl'

# Path to the compressed .pkl.bz2 file
output_file = 'movie_recommender\similarity.pkl.bz2'

with open(input_file, 'rb') as f_in, bz2file.BZ2File(output_file, 'wb') as f_out:
    f_out.write(f_in.read())

print(f'Compressed file saved as {output_file}')
