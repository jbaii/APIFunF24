import pickle

interview_header = ["level", "lang", "tweets", "phd"]
interview_tree = ['Attribute', 'level', ['Value', 'Junior', ['Attribute', 'phd', ['Value', 'yes', ['Leaf', 'False', 2, 5]], ['Value', 'no', ['Leaf', 'True', 3, 5]]]], ['Value', 'Mid', ['Leaf', 'True', 4, 14]], ['Value', 'Senior', ['Attribute', 'tweets', ['Value', 'yes', ['Leaf', 'True', 2, 5]], ['Value', 'no', ['Leaf', 'False', 3, 5]]]]]

# pickle (object serialization): saving a binary representation of an object
# in file for feature and using later
# example: saving a traning a model for inference/orediction later
# in another python process, possibly running on a diff machine(server)
# imagine you just trained an awesome MyRandomForestClassifier
# and now you need to save it for using in your web app on a server later





packaged_obj = {interview_header, interview_tree}
outfile = open("tree.p", "wb")
pickle.dump(packaged_obj, outfile)
outfile.close()
