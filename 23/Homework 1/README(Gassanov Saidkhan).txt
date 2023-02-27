Overwiew.
Customer: speakers, civil servants, comedians, etc.
Goal: to help with speeches.
Pains: lack of a suitable dataset.
Gains: will help to find the right emotion for the speech.

Value proposition.
Product: a service on the right emotions.
Alleviates: will help pick up the emotion.
Advantages: clients do not have to think about emotions during the performance.

Objectives.
Allow clients to add their own prescribed texts.
[OUR FOCUS] Getting the emotion right. 


Solution.
Develop a model capable of classifying incoming content so that it can be organised.

Core features:

ML service that will predict the correct categories for inbound content. [OUR FOCUS.]
User feedback process for incorrectly categorised content.

Integrations:
Classified content will be sent to the UI service for display.
textual feedback from users will be sent to development.

Alternatives:
Allow users to add content manually (bottleneck).

Constraints:
Maintain low latency (>100ms) when classifying incoming content. [Latency].

Feasibility.
We have a data set that we will use.

Engineering.
We have developed our own approach to creating our product.

Data.
Training:
access to raw data for training.
was any sampling used to create this dataset?
no data leakage?

Production:
access to timely batches of ML content from sources.
how can we trust that this stream contains only data that is consistent with what we have seen in the past?

Labeling.
Labelling: labelling using machine learning categories.

Features: textual characteristics.

Labels: reflect the categories of content we currently display on our platform.

Evaluation.
Offline evaluation: We will take some of the data from the dataset to evaluate the performance of the model.
Online evaluation: Allow users to report misclassified content by our model.

Modelingю 
Use some model from https://paperswithcode.com/task/speech-emotion-recognition.

Feedback. 
Allow users to report misclassified content by our model.

Team. 
product: Product managers, Executives

system design:
Data collectors: Collect the necessary data and label it. 
Machine learner: Develops the ML model.
Designer: Designs UX/UI for the application.
Programmer: Develops the application.
Testers: Test the application before release.

project: Team leader, Project manager

Deliverables.

Objective			Priority	Release		Status
Create an English emotion       High            v1 
recognition algorithm and 
application for easy access.
  
Deliverable	    Contributors	     Dependencies		Acceptance criteria	   Status		Timelines

Labeled         Data collectors,   Unlabeled data       Valid dataset         In-progress        2 weeks
dataset for     labeling team
training

Trained model   Machine Learner    Labeled dataset      Evoluation results    In-progress        1 week

Design of
the application Designer           Information about    Modern comfortable    In-progress        1 week
|  |  |  |  |  |  |  |  |  |  |  | the project          design

Application     Programmer,        UX/UI design         Working application     
In-progress     1.5 week
|  |  |  |  |  |Machine learner
|
Testing         Testers            Application          Positive ratings        In-progress     1 week
|  |  |  |  |  |  |  |  |  |  | and a minimum 
|  |  |  |  |  |  |  |  |  |  | number of bugs

Production      Product managers,  Tested application   Release of the		
In-progress     2 weeks
|  |  Advertisers			application to
|  |  |  |  |  |  |  | production



