from vast.types import VFundamentalType, VPointerType, Constness
from vast.declarations import VFunction, VArgument
from vast.scope import Scope

fundamental_types = {
    "Int8":    VFundamentalType(VFundamentalType.T.INT,   VFundamentalType.Bits.b8),
    "Int16":   VFundamentalType(VFundamentalType.T.INT,   VFundamentalType.Bits.b16),
    "Int32":   VFundamentalType(VFundamentalType.T.INT,   VFundamentalType.Bits.b32),
    "Int64":   VFundamentalType(VFundamentalType.T.INT,   VFundamentalType.Bits.b64),
    "UInt8":   VFundamentalType(VFundamentalType.T.UINT,  VFundamentalType.Bits.b8),
    "UInt16":  VFundamentalType(VFundamentalType.T.UINT,  VFundamentalType.Bits.b16),
    "UInt32":  VFundamentalType(VFundamentalType.T.UINT,  VFundamentalType.Bits.b32),
    "UInt64":  VFundamentalType(VFundamentalType.T.UINT,  VFundamentalType.Bits.b64),
    "Float32": VFundamentalType(VFundamentalType.T.FLOAT, VFundamentalType.Bits.b32),
    "Float64": VFundamentalType(VFundamentalType.T.FLOAT, VFundamentalType.Bits.b64),
}

util_types = {
    "CString": VPointerType(fundamental_types["Int8"], VPointerType.Kind.POINTER, Constness.CONSTANT),
}


functions = {
    # Made into an intrinsic until I introduce externs to grammar, so I can do a quick "Hello, World!"
    "PutCString": VFunction(
        name="PutCString", extern_kind=VFunction.ExternKind.C, extern_name="puts",
        return_type=fundamental_types["Int32"],
        targets=[],
        args=[
            VArgument(name="string", type=util_types["CString"], init_value=None),
        ],
        body=None
    )
}

intrinsic_scope = Scope.from_dict({
    **fundamental_types,
    **util_types,
    **functions,
})

