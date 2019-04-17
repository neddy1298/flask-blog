from flask import Blueprint, jsonify, request
from flaskblog.models import Post, User, UserSchema, PostSchema, MenuSchema, HotelSchema, KamarSchema, Hotel, Kamar, Menu
from flask_login import login_required, current_user

api = Blueprint('api', __name__)
menus_schema = MenuSchema(many=True, strict=True)
menu_schema = UserSchema(strict=True)
kamars_schema = KamarSchema(many=True, strict=True)
kamar_schema = UserSchema(strict=True)
hotels_schema = HotelSchema(many=True, strict=True)
hotel_schema = UserSchema(strict=True)
users_schema = UserSchema(many=True, strict=True)
user_schema = UserSchema(strict=True)
posts_schema = PostSchema(many=True, strict=True)
post_schema = PostSchema(strict=True)


########################################################################
############################# G E T ####################################
########################################################################

@api.route("/api/menu", methods=['GET'])
@login_required
def menu():
	menu = Menu.query.all()
	result = menus_schema.dump(menu)
	return jsonify(result.data)

@api.route("/api/hotel", methods=['GET'])
@login_required
def hotel():
	hotel = Hotel.query.all()
	result = hotels_schema.dump(hotel)
	return jsonify(result.data)

@api.route("/api/kamar", methods=['GET'])
@login_required
def kamar():
	kamar = Kamar.query.all()
	result = kamars_schema.dump(kamar)
	return jsonify(result.data)


@api.route("/api/user/<id>", methods=['GET'])
@login_required
def user(id):
	user = User.query.get(id)
	return user_schema.jsonify(user)

@api.route("/api/user/all", methods=['GET'])
@login_required
def users():
	all_user = User.query.all()
	result = users_schema.dump(all_user)
	return jsonify(result.data)

@api.route("/api/post/<user_id>", methods=['GET'])
@login_required
def post(user_id):
	posts = Post.query.filter_by(user_id=user_id)
	result = posts_schema.dump(posts)
	return jsonify(result.data)

@api.route("/api/post/all", methods=['GET'])
@login_required
def posts():
	all_post = Post.query.all()
	result = posts_schema.dump(all_post)
	return jsonify(result.data)

########################################################################
########################### P O S T ####################################
########################################################################

@api.route('/api/menu/add', methods=['POST'])
def add_menu():
	menu = request.json['menu']
	keterangan = request.json['keterangan']
	image_file = request.json['image_file']

	new_menu = Menu(menu, keterangan, image_file)

	db.session.add(new_menu)
	db.session.commit()

	return menu_schema.jsonify(new_menu)

@api.route('/api/kamar/add', methods=['POST'])
def add_kamar():
	nama = request.json['nama']
	image_file = request.json['image_file']
	fasilitas = request.json['fasilitas']
	harga = request.json['harga']
	stok = request.json['stok']

	new_kamar = Menu(nama,image_file,fasilitas,harga,stok)

	db.session.add(new_kamar)
	db.session.commit()

	return kamar_schema.jsonify(new_kamar)

@api.route('/api/hotel/add', methods=['POST'])
def add_hotel():
	nama = request.json['nama']
	alamat = request.json['alamat']
	image_file = request.json['image_file']

	new_hotel = Menu(nama, alamat, image_file)

	db.session.add(new_hotel)
	db.session.commit()

	return hotel_schema.jsonify(new_hotel)

@api.route('/api/user/add', methods=['POST'])
def add_user():
	username = request.json['username']
	email = request.json['email']
	image_file = request.json['image_file']
	password = request.json['password']

	new_user = Menu(menu, email, image_file ,password)

	db.session.add(new_user)
	db.session.commit()

	return user_schema.jsonify(new_user)

@api.route('/api/post/add', methods=['POST'])
def add_post():
	title = request.json['title']
	date_posted = request.json['keterangan']
	content = request.json['content']
	user_id = request.json['user_id']

	new_post = Menu(title, date_posted, content, user_id)

	db.session.add(new_post)
	db.session.commit()

	return post_schema.jsonify(new_post)


########################################################################
############################# P U T ####################################
########################################################################

@api.route('/api/menu/edit/<id>', methods=['PUT'])
def edit_menu(id):
	menu = Menu.query.get(id)

	new_menu = request.json['menu']
	keterangan = request.json['keterangan']
	image_file = request.json['image_file']

	menu.menu = new_menu
	menu.keterangan = keterangan
	menu.image_file = image_file

	db.session.commit()

	return menu_schema.jsonify(menu)

@api.route('/api/kamar/edit/<id>', methods=['PUT'])
def edit_kamar(id):
	kamar = Kamar.query.get(id)

	nama = request.json['nama']
	image_file = request.json['image_file']
	fasilitas = request.json['fasilitas']
	harga = request.json['harga']
	stok = request.json['stok']

	kamar.nama = nama
	kamar.image_file = image_file
	kamar.fasilitas = fasilitas
	kamar.harga = harga
	kamar.stok = stok

	db.session.commit()

	return kamar_schema.jsonify(kamar)

@api.route('/api/hotel/edit/<id>', methods=['PUT'])
def edit_hotel(id):
	hotel = Hotel.query.get(id)
	nama = request.json['nama']
	alamat = request.json['alamat']
	image_file = request.json['image_file']

	hotel.nama = nama
	hotel.alamat = alamat
	hotel.image_file = image_file

	db.session.commit()

	return hotel_schema.jsonify(hotel)

@api.route('/api/user/edit/<id>', methods=['PUT'])
def edit_user(id):
	user = User.query.get(id)
	username = request.json['username']
	email = request.json['email']
	image_file = request.json['image_file']
	password = request.json['password']

	user.username = username
	user.email = email
	user.image_file = image_file
	user.password = password

	db.session.commit()

	return user_schema.jsonify(user)

@api.route('/api/post/edit/<id>', methods=['PUT'])
def edit_post(id):
	post = Post.query.get(id)
	title = request.json['title']
	date_posted = request.json['keterangan']
	content = request.json['content']
	user_id = request.json['user_id']

	post.title = title
	post.date_posted = date_posted
	post.content = content
	post.user_id = user_id

	db.session.commit()

	return post_schema.jsonify(post)

########################################################################
########################## D E L E T E #################################
########################################################################

@api.route('/api/menu/delete/<id>', methods=['DELETE'])
def delete_menu(id):
	menu = Menu.query.get(id)
	db.session.delete(menu)
	db.session.commit()

	return menu_schema.jsonify(menu)

@api.route('/api/kamar/delete/<id>', methods=['DELETE'])
def delete_kamar(id):
	kamar = Kamar.query.get(id)
	db.session.delete(kamar)
	db.session.commit()

	return kamar_schema.jsonify(kamar)

@api.route('/api/hotel/delete/<id>', methods=['DELETE'])
def delete_hotel(id):
	hotel = Hotel.query.get(id)
	db.session.delete(hotel)
	db.session.commit()

	return hotel_schema.jsonify(hotel)

@api.route('/api/user/delete/<id>', methods=['DELETE'])
def delete_user(id):
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()

	return user_schema.jsonify(user)

@api.route('/api/post/delete/<id>', methods=['DELETE'])
def delete_post(id):
	post = Post.query.get(id)
	db.session.delete(post)
	db.session.commit()

	return post_schema.jsonify(post)