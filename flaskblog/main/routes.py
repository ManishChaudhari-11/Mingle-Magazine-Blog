from flask import Blueprint, redirect, render_template, request, url_for

from flaskblog import params
from flaskblog.models import Post

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    category = request.args.get("category", type=str, default=None)
    posts = Post.query.all()
    categories = []
    for post in posts:
        categories.append(post.category)
    categories = list(set(categories))
    categories.sort()
    if category is None:
        posts = Post.query.order_by(Post.date_posted.desc()).paginate(
            page=page, per_page=params["posts_per_page"]
        )
    else:
        posts = (
            Post.query.filter_by(category=category)
            .order_by(Post.date_posted.desc())
            .paginate(page=page, per_page=params["posts_per_page"])
        )
    # print(paragraphs)
    return render_template(
        "home.html",
        posts=posts,
        params=params,
        post_categories=categories,
        post_category=category,
    )


@main.route("/about")
def about():
    return render_template("about.html", title="About", params=params)


@main.route("/calendar")
def calendar():
    return render_template("calendar.html", title="Calendar", params=params)
