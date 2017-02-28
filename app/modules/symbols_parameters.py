from flask_restplus import reqparse

def symbol_parameters():
    parser = reqparse.RequestParser()
    parser.add_argument('symbol',
                        type=list,
                        required=False,
                        location="json",
                        help="limit a number of items (allowed range is 1-100), default is 20.")

    parser.add_argument('offset',
                        type=int,
                        required=False,
                        default=0,
                        help="a number of items to skip, default is 0.")
    
    return parser
