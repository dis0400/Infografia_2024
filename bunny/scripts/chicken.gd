extends CharacterBody2D

@export var target: Node2D = null
@export var max_speed = 50
@onready var navigation: NavigationAgent2D = $NavigationAgent2D

func setup():
	await get_tree().physics_frame
	update_target_to_nearest_egg()

func _ready() -> void:
	call_deferred("setup")
	print(navigation.get_current_navigation_path())
	
func _physics_process(delta: float) -> void:
	update_target_to_nearest_egg()

	
	if navigation.is_navigation_finished():
		return
	
	var nex_path_position = navigation.get_next_path_position()
	
	velocity = global_position.direction_to(nex_path_position) * max_speed
	
	move_and_slide()
	
	

func update_target_to_nearest_egg() -> void:
	var nearest_egg = find_nearest_egg()
	if nearest_egg:
		navigation.target_position = nearest_egg.global_position


func find_nearest_egg() -> Node2D:
	var eggs = get_tree().get_nodes_in_group("eggs")
	var nearest_egg: Node2D = null
	var min_distance = INF

	for egg in eggs:
		var distance = global_position.distance_to(egg.global_position)
		if distance < min_distance:
			min_distance = distance
			nearest_egg = egg
	
	return nearest_egg
