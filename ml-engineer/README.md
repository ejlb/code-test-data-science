# ML Engineer Code Test

The `email_similarity` package contains two functions

* `api.email_similarity` takes in two email addresses and returns a similarity score. 
* `features.features` takes in a single email address and returns a feature vector.

The similarity score, by default, is the cosine distance between the email address feature vectors. You may modify this function as part of the test if you desire. The feature vectors are calculated in `features.features`. Your main job is to implement `features.features`. You can run `eval.py` to get a score for how well your features measure email address similarity (see `eval.py` for more details). After you submit your solution, we will test your features against additional data to gauge how well your features generalise.
