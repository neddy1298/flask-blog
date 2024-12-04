from flask import Blueprint, jsonify, request, abort
from flaskblog.models import Post, User, UserSchema, PostSchema, MenuSchema, HotelSchema, KamarSchema, Hotel, Kamar, Menu
from flask_login import login_required, current_user
from flaskblog import db
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

api = Blueprint('api', __name__)

# Schemas with more robust configuration
menus_schema = MenuSchema(many=True)
menu_schema = MenuSchema()
kamars_schema = KamarSchema(many=True)
kamar_schema = KamarSchema()
hotels_schema = HotelSchema(many=True)
hotel_schema = HotelSchema()
users_schema = UserSchema(many=True)
user_schema = UserSchema()
posts_schema = PostSchema(many=True)
post_schema = PostSchema()

########################################################################
############################# G E T ####################################
########################################################################

@api.route("/api/menu", methods=['GET'])
@login_required
def get_menus():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    menus = Menu.query.paginate(page=page, per_page=per_page)
    result = menus_schema.dump(menus.items)
    return jsonify({
        'items': result,
        'total': menus.total,
        'page': page,
        'per_page': per_page
    })

@api.route("/api/hotel", methods=['GET'])
@login_required
def get_hotels():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    hotels = Hotel.query.paginate(page=page, per_page=per_page)
    result = hotels_schema.dump(hotels.items)
    return jsonify({
        'items': result,
        'total': hotels.total,
        'page': page,
        'per_page': per_page
    })

@api.route("/api/kamar", methods=['GET'])
@login_required
def get_kamars():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    kamars = Kamar.query.paginate(page=page, per_page=per_page)
    result = kamars_schema.dump(kamars.items)
    return jsonify({
        'items': result,
        'total': kamars.total,
        'page': page,
        'per_page': per_page
    })

@api.route("/api/user/<int:id>", methods=['GET'])
@login_required
def get_user(id):
    user = User.query.get_or_404(id, description='User not found')
    return user_schema.jsonify(user)

@api.route("/api/user/all", methods=['GET'])
@login_required
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    users = User.query.paginate(page=page, per_page=per_page)
    result = users_schema.dump(users.items)
    return jsonify({
        'items': result,
        'total': users.total,
        'page': page,
        'per_page': per_page
    })

@api.route("/api/post/<int:user_id>", methods=['GET'])
@login_required
def get_posts(user_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    posts = Post.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)
    result = posts_schema.dump(posts.items)
    return jsonify({
        'items': result,
        'total': posts.total,
        'page': page,
        'per_page': per_page
    })

@api.route("/api/post/all", methods=['GET'])
@login_required
def get_all_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    posts = Post.query.paginate(page=page, per_page=per_page)
    result = posts_schema.dump(posts.items)
    return jsonify({
        'items': result,
        'total': posts.total,
        'page': page,
        'per_page': per_page
    })

########################################################################
########################### P O S T ####################################
########################################################################

@api.route("/api/menu", methods=['POST'])
@login_required
def add_menu():
    try:
        data = menu_schema.load(request.json)
        menu = Menu(**data)
        db.session.add(menu)
        db.session.commit()
        return menu_schema.jsonify(menu), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Menu already exists'}), 409

@api.route("/api/hotel", methods=['POST'])
@login_required
def add_hotel():
    try:
        data = hotel_schema.load(request.json)
        hotel = Hotel(**data)
        db.session.add(hotel)
        db.session.commit()
        return hotel_schema.jsonify(hotel), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Hotel already exists'}), 409

@api.route("/api/kamar", methods=['POST'])
@login_required
def add_kamar():
    try:
        data = kamar_schema.load(request.json)
        kamar = Kamar(**data)
        db.session.add(kamar)
        db.session.commit()
        return kamar_schema.jsonify(kamar), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Kamar already exists'}), 409

@api.route("/api/user", methods=['POST'])
@login_required
def add_user():
    try:
        data = user_schema.load(request.json)
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user_schema.jsonify(user), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User already exists'}), 409

@api.route("/api/post", methods=['POST'])
@login_required
def add_post():
    try:
        data = post_schema.load(request.json)
        post = Post(**data)
        db.session.add(post)
        db.session.commit()
        return post_schema.jsonify(post), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Post already exists'}), 409

########################################################################
############################# P U T ####################################
########################################################################

@api.route("/api/menu/<int:id>", methods=['PUT'])
@login_required
def edit_menu(id):
    menu = Menu.query.get_or_404(id, description='Menu not found')
    try:
        data = menu_schema.load(request.json)
        menu.menu = data['menu']
        menu.keterangan = data['keterangan']
        menu.image_file = data['image_file']
        db.session.commit()
        return menu_schema.jsonify(menu)
    except ValidationError as err:
        return jsonify(err.messages), 400

@api.route("/api/hotel/<int:id>", methods=['PUT'])
@login_required
def edit_hotel(id):
    hotel = Hotel.query.get_or_404(id, description='Hotel not found')
    try:
        data = hotel_schema.load(request.json)
        hotel.nama = data['nama']
        hotel.alamat = data['alamat']
        hotel.image_file = data['image_file']
        db.session.commit()
        return hotel_schema.jsonify(hotel)
    except ValidationError as err:
        return jsonify(err.messages), 400

@api.route("/api/kamar/<int:id>", methods=['PUT'])
@login_required
def edit_kamar(id):
    kamar = Kamar.query.get_or_404(id, description='Kamar not found')
    try:
        data = kamar_schema.load(request.json)
        kamar.nama = data['nama']
        kamar.image_file = data['image_file']
        kamar.fasilitas = data['fasilitas']
        kamar.harga = data['harga']
        kamar.stok = data['stok']
        db.session.commit()
        return kamar_schema.jsonify(kamar)
    except ValidationError as err:
        return jsonify(err.messages), 400

@api.route("/api/user/<int:id>", methods=['PUT'])
@login_required
def edit_user(id):
    user = User.query.get_or_404(id, description='User not found')
    try:
        data = user_schema.load(request.json)
        user.username = data['username']
        user.email = data['email']
        user.image_file = data['image_file']
        user.password = data['password']
        db.session.commit()
        return user_schema.jsonify(user)
    except ValidationError as err:
        return jsonify(err.messages), 400

@api.route("/api/post/<int:id>", methods=['PUT'])
@login_required
def edit_post(id):
    post = Post.query.get_or_404(id, description='Post not found')
    try:
        data = post_schema.load(request.json)
        post.title = data['title']
        post.date_posted = data['date_posted']
        post.content = data['content']
        post.user_id = data['user_id']
        db.session.commit()
        return post_schema.jsonify(post)
    except ValidationError as err:
        return jsonify(err.messages), 400

########################################################################
########################## D E L E T E #################################
########################################################################

@api.route("/api/menu/<int:id>", methods=['DELETE'])
@login_required
def delete_menu(id):
    menu = Menu.query.get_or_404(id, description='Menu not found')
    db.session.delete(menu)
    db.session.commit()
    return menu_schema.jsonify(menu)

@api.route("/api/hotel/<int:id>", methods=['DELETE'])
@login_required
def delete_hotel(id):
    hotel = Hotel.query.get_or_404(id, description='Hotel not found')
    db.session.delete(hotel)
    db.session.commit()
    return hotel_schema.jsonify(hotel)

@api.route("/api/kamar/<int:id>", methods=['DELETE'])
@login_required
def delete_kamar(id):
    kamar = Kamar.query.get_or_404(id, description='Kamar not found')
    db.session.delete(kamar)
    db.session.commit()
    return kamar_schema.jsonify(kamar)

@api.route("/api/user/<int:id>", methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get_or_404(id, description='User not found')
    db.session.delete(user)
    db.session.commit()
    return user_schema.jsonify(user)

@api.route("/api/post/<int:id>", methods=['DELETE'])
@login_required
def delete_post(id):
    post = Post.query.get_or_404(id, description='Post not found')
    db.session.delete(post)
    db.session.commit()
    return post_schema.jsonify(post)