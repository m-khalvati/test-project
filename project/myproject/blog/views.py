from django.shortcuts import render

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    data = [
        {
          "title": "Abraham Lincoln",
          "dis": "Abraham Lincoln was the 16th President of the United States, serving from March 1861 until his assassination in April 1865. He is best known for leading the country during the American Civil War and for his efforts to end slavery"
        },
        {
          "title": "Martin Luther King Jr.",
          "dis": "Martin Luther King Jr. was an American Baptist minister and activist who played a pivotal role in the Civil Rights Movement. He is best known for his leadership in the movement and his famous 'I Have a Dream' speech."
        }
      ]
    return render(request, 'blog/about.html', { "data": data })

# def index(request):
  
#   return render(request, 'blog/index.html', { "data": data })